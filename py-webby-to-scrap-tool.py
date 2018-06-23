# imported libraries 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

from datetime import datetime
import csv

# Beautiful Soup Use Case Example

base_url = "https://www.seek.com.au/software-developer-jobs/in-All-Sydney-NSW"

#query website and return html to the page
page = urlopen(base_url)

soup = BeautifulSoup(page)

# prettify the html string content 
html_str = soup.prettify()

# then write the content to a local html file
html_file = open('base_url.html', 'w')
html_file.write(html_str)
html_file.close()

# Open up the newly written html file
# try:
#   file_name = "file:///Users/andywongcm/Documents/Github/py-webby-to-scrap-tool/base_url.html"
#   webbrowser.open_new_tab(file_name)
# except:
#   print("Cannot open local file: {0}".format(file_name))

def fetch_articles():
  return soup.find_all("article")

def extract_details(a_job_article, csv_writer=None):
  job_article_dict = {}

  # Job title
  print(a_job_article["aria-label"])
  job_article_dict["job_title"] = a_job_article["aria-label"]

  # Company
  company = a_job_article.find(attrs={"data-automation":"jobCompany"}) 
  if company !=  None:
    print(company.text)
    job_article_dict["company"] = company.text

  # Location
  location = a_job_article.find(attrs={"data-automation":"jobLocation"}) 
  if location !=  None:
    print(location.text)
    job_article_dict["location"] = location.text

  # Area
  area = a_job_article.find(attrs={"data-automation":"jobArea"}) 
  if area !=  None:
    print(area.text)
    job_article_dict["area"] = area.text
  
  # Salary range
  salary = a_job_article.find(attrs={"data-automation":"jobSalary"}) 
  if salary !=  None:
    print(salary.text)
    job_article_dict["salary_range"] = salary.text
  
  # Duties and tasks(optional)
  if a_job_article.find('ul') != None:
    dutiestasks_list = a_job_article.find('ul').find_all('li')
    list_of_dutiestasks = []
    if dutiestasks_list != None:  
      for dutiestasks_item in dutiestasks_list:
        if dutiestasks_item !=  None:
          print(dutiestasks_item.text)
          list_of_dutiestasks.append(dutiestasks_item.text)
      job_article_dict["role_specification"] = ';'.join(list_of_dutiestasks)
  else:
    job_article_dict["role_specification"] = ""
      
  # Job Description
  job_description = a_job_article.find(attrs={"data-automation":"jobShortDescription"}) 
  if job_description !=  None:
    print(job_description.text)
    job_article_dict["job_description"] = job_description.text

  # Grab the actual job post link 
  job_link = a_job_article.find(attrs={"data-automation":"jobTitle"})
  if job_link != None:
    print(job_link)
    # only gives you the relative link url.
    job_article_dict["job_link"] = job_link['href']

  csv_writer.writerow(job_article_dict)

# Writes to CSV report file
with open('base_url_semantics.csv', 'a') as csv_file:
  # Empty file contents first
  csv_file.seek(0)
  csv_file.truncate()

  fieldnames = ['job_title', 'company', 'location', 'area', 'salary_range', 'role_specification', 'job_description', 'job_link']
  csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  csv_writer.writeheader()
  
  job_articles = fetch_articles()

  for a_job_article in job_articles:
    extract_details(a_job_article, csv_writer)
  
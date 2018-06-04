# imported libraries 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

from datetime import datetime
import csv

base_url = "https://www.seek.com.au/software-developer-jobs/in-All-Sydney-NSW"

#query website and return html to the page
page = urlopen(base_url)

soup = BeautifulSoup(page)

# what you see the actual html content
html_str = soup.prettify()
print(html_str)

# then write the content to a local html file
html_file = open('base_url.html', 'w')
html_file.write(html_str)
html_file.close()

# Write to new file
try:
  file_name = "file:///Users/andywongcm/Documents/Github/py-webby-to-scrap-tool/base_url.html"
  webbrowser.open_new_tab(file_name)
except:
  print("Cannot open local file: {0}".format(file_name))


def decide_output_type(output_str, csv_file_writer=None):
  if csv_file_writer is not None:
    csv_file_writer.writerow([output_str])
  else:
    print(output_str)

def search_and_output_tag(of_tag_type, title, attr_type, csv_file_writer=None):
  main_title = "=== {0} ===".format(title)
  decide_output_type(main_title, csv_file_writer)
  all_tags = soup.find_all(of_tag_type)
  for tag in all_tags:
    tag_output_str = determine_type(tag, attr_type)
    decide_output_type(tag_output_str, csv_file_writer)
  total_tag_count_str = "Total {0} items: {1}".format(of_tag_type.upper(), len(all_tags))
  decide_output_type(total_tag_count_str, csv_file_writer)

def determine_type(tag_obj, tag_type):
  output_str = None
  if tag_type == "text":
    output_str = "Content: {0}".format(tag_obj.text)
  elif tag_type == "href":
    output_str = "Link: {0} ".format(tag_obj.get("href"))
  elif tag_type == "image":
    output_str = "Image: {0} , Alt: {1}".format(tag_obj.attrs['src'] , tag_obj.get('alt',''))
  return output_str

def fetch_articles():
  return soup.find_all("article")

def extract_details(a_job_article):
  # Job title
  print(a_job_article["aria-label"])

  # Company
  company = a_job_article.find(attrs={"data-automation":"jobCompany"}) 
  if company !=  None:
    print(company.text)

  # Location
  company = a_job_article.find(attrs={"data-automation":"jobCompany"}) 
  if company !=  None:
    print(company.text)

  # Job Type
  company = a_job_article.find(attrs={"data-automation":"jobCompany"}) 
  if company !=  None:
    print(company.text)
  
  # Job Description
  company = a_job_article.find(attrs={"data-automation":"jobCompany"}) 
  if company !=  None:
    print(company.text)

# Writes to CSV report file
with open('base_url_semantics.csv', 'a') as csv_file:
  # Empty file contents first
  csv_file.seek(0)
  csv_file.truncate()

  csv_writer = csv.writer(csv_file)
  
  csv_writer.writerow(["==== Title ===="])
  csv_writer.writerow([soup.title.text])
  
  job_articles = fetch_articles()

  for a_job_article in job_articles:
    extract_details(a_job_article)
  
# imported libraries 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

from datetime import datetime
import csv

'''
TODOS
A tool to takes a url content and scrap 3 data infomration on the page.
h1 - heading
url - url link
p - paragraph
img - images
'''
base_url = "https://www.sbs.com.au/popasia/blog/2017/08/23/youtube-helping-push-k-pop-mainstream"

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

# Prints output to console screen
print("==== Title ====")
print(soup.title.text)
search_and_output_tag("h1", "H1 Titles", "text")
search_and_output_tag("h2", "H2 Titles", "text")
search_and_output_tag("p", "Paragraphs content", "text")
search_and_output_tag("a", "Hyperlink links", "href")
search_and_output_tag("img", "Images", "image")

# Writes to CSV report file
with open('base_url_semantics.csv', 'a') as csv_file:

  # Empty file contents first
  csv_file.seek(0)
  csv_file.truncate()

  csv_writer = csv.writer(csv_file)
  
  csv_writer.writerow(["==== Title ===="])
  csv_writer.writerow([soup.title.text])
  
  search_and_output_tag("h1", "H1 Titles", "text", writer)
  search_and_output_tag("h2", "H2 Titles", "text", writer)
  search_and_output_tag("p", "paragraphs content", "text", writer)
  search_and_output_tag("a", "a links", "href", writer)
  search_and_output_tag("img", "images", "image", writer)

  
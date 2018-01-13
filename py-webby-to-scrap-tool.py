# library to query website using standard HTTP protocol
'''
TODOS
A tool to takes a url content and scrap 3 data infomration on the page.
h1 - heading
url - url link
p - paragraph

'''
from urllib.request import urlopen

from bs4 import BeautifulSoup

wiki = "https://www.billboard.com/articles/columns/k-town/7873405/mrshll-gay-artist-korea-kpop"

#query website and return html to the variable
page = urlopen(wiki)

soup = BeautifulSoup(page)

print(soup.prettify())

print("==== Title ====")
print(soup.title)
print("=== h1 Titles ===")
for h1_title in soup.find_all("h1"):
  print("H1: %s" % h1_title.text)

print("==== h2 Titles ====")
for h2_title in soup.find_all("h2"):
  print("H2: %s" % h2_title.text)

print("==== paragraphs  content ====")
all_paragraphs = soup.find_all("p")
for paragraph in all_paragraphs:
  print("Paragraph: %s " % paragraph.text)

print("==== a links ====")
all_links = soup.find_all("a")
for link in all_links:
  print("Links: %s " % link.get("href"))

print("==== images ====")
all_images = soup.find_all("img")
for image in all_images:
  print("Image: {0} , Alt: {1}".format(image.attrs['src'] , image.get('alt','')))


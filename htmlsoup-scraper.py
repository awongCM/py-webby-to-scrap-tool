# TODO - OOD class
# 1. One for reading the locally written html
# 2. One for parsing html content and writing its CSV content

from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv

base_url = "https://www.seek.com.au/lead-developer-jobs/in-All-Sydney-NSW"


class HTMLSoupScraper:
    html_output = "main_url.html"

    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.page_content = ''

    def open_url(self):
        return BeautifulSoup(urlopen(self.baseurl), features="lxml")

    def output_html_content(self):
        soup = self.open_url()
        self.page_content = soup.prettify()

    def write_content_to_file(self, option):
        html_file = open(self.html_output, option)
        html_file.write(self.page_content)
        html_file.close()

    def __str__(self):
        return f'{self.html_output} will be printed'


if __name__ == "__main__":
    html_soup_scraper = HTMLSoupScraper(base_url)
    html_soup_scraper.output_html_content()
    html_soup_scraper.write_content_to_file('w')

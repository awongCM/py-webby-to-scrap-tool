# TODO - class to implement

from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

from datetime import datetime
import csv

class HTMLSoupScraper:
  
  def __init__(self, baseurl):
    raise NotImplementedError
  
  def open_url(self, parameter_list):
    pass

  def output_html_content(self, parameter_list):
    pass

  def write_content_to_file(parameter_list):
    pass
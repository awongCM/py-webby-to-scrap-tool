# Simple web-scraping tool written in Python

## Ingredients used for making this tool
1. Beautiful Soup
2. Scrapy

My very own implementation in scraping and extracting web content, and exporting them into CSV files.

### To run samples

#### BeautifulSoup

1. Download the project folder, if you haven't done so.
2. Navigate to the project folder
3. Run `python py-webby-to-scrap-tool.py`

#### Scrapy

1. Download the project folder, if you haven't done so.
2. Navigate to `jobsearchscarper` folder
3. Run `scrapy runspider ./jobsearchscaper/spiders/job_search_spider.py`
4. To export to CSV files, you run `scrapy crawl job_searches -o job_searches.csv`

#### TODOs
1. Add some unit testing code in place!! - (Hint: use unittest or pytest)
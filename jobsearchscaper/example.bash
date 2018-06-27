## USEFUL COMMANDS 

# To begin crawling and scraping (without exporting) 
scrapy runspider ./jobsearchscaper/spiders/job_search_spider.py


# To begin crawling and scraping (exporting to csv)
scrapy crawl job_searches -o job_searches.csv
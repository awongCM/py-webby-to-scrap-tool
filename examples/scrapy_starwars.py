import scrapy

class StarWarsSpider(scrapy.Spider):
    name = 'starwars'
    allowed_domains = ["starwars.com"]
    start_urls = ['https://www.starwars.com/databank']

    
    def parse(self, response):
      # TODO - to investigate why this line of css selector code does not work on starwars site!!?
      # urls = response.css('.blocks-container.ref-1-3 .building-block-config .image-wrapper a::attr(href)').extract()
      urls = response.css('.building-block-config .image-wrapper a::attr(href)').extract()
      
      for url in urls:
    	  url = response.urljoin(url)
    	  yield scrapy.Request(url=url, callback=self.parse_details)

    
    def parse_details(self, response):
      # TODO - why did the character text returns null??
    	yield {
    	      'Image': response.css('.ratio-16x9 .building-block .image-wrapper .aspect img::attr(src)').extract_first(),
            'Character': response.css('.ratio-16x9 .building-block .content-wrapper .content-info .title span::text').extract_first(),
      }
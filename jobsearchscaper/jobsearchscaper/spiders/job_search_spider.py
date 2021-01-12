import scrapy

# Scrapy Use Case Example


class JobSearchSpider(scrapy.Spider):
    name = "job_searches"
    allowed_domains = ["seek.com.au"]
    start_urls = [
        # "https://www.seek.com.au/software-developer-jobs/in-All-Sydney-NSW?sortmode=ListedDate" -- old
        "https://www.seek.com.au/lead-developer-jobs/in-All-Sydney-NSW"
    ]

    def parse(self, response):
        self.log('Browsing ' + response.url)
        job_articles = response.css('article')

        for job in job_articles:
            list_of_dutiestasks = []
            duties_list = job.css('ul li')
            for each_duty in duties_list:
                list_of_dutiestasks.append(
                    each_duty.css('span::text').extract_first()
                )

            item = {}
            item['job_listing_date'] = job.css(
                'span[data-automation="jobListingDate"]::text').extract_first()
            item['job_title'] = job.css(
                'article::attr(aria-label)').extract_first()
            item['company'] = job.css(
                'a[data-automation="jobCompany"]::text').extract_first()
            item['location'] = job.css(
                'a[data-automation="jobLocation"]::text').extract_first()
            item['area'] = job.css(
                'a[data-automation="jobArea"]::text').extract_first()
            item['salary_range'] = job.css(
                'span[data-automation="jobSalary"] span::text').extract_first()
            if len(list_of_dutiestasks) != 0:
                item['role_specification'] = ';'.join(list_of_dutiestasks)
            else:
                item['role_specification'] = ''
            item['job_description'] = job.css(
                'span[data-automation="jobShortDescription"] span[data-automation="false"]::text').extract_first()
            # Grab the actual job post link
            item['job_link'] = response.urljoin(
                job.css('a[data-automation="jobTitle"]::attr(href)').extract_first())

            yield item

        # following paginations
        next_page_url = response.css(
            'a[data-automation="page-next"]::attr(href)').extract_first()
        self.log("Next page url to navigate: " + next_page_url)
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

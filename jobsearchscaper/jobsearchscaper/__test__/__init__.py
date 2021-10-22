# TODO - https://stackoverflow.com/questions/6456304/scrapy-unit-testing/12741030#12741030]
import unittest
from jobsearchscaper.spiders import JobSearchSpider
from responses import fake_response_from_file


class JobSearchSpiderTestCase(unittest.TestCase):
    """docstring for JobSearchSpiderTestCase."""

    def setUp(self):
        self.spider = JobSearchSpider(l)

    def _test_yielded_items(self, results, expected_length):
        count = 0
        for job_article in results:
            self.assertIsNotNone(job_article['job_listing_date'])
            self.assertIsNotNone(job_article['job_title'])
        self.assertEqual(count, expected_length)

    def test_parse(self):
        job_articles = self.spider.parse(
            fake_response_from_file('some_file_i_need_to_generate_from'))
        self._test_yielded_items(job_articles, 10)


if __name__ == "__main__":
    unittest.main()

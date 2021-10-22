
# TODO - Credit goes for - https://stackoverflow.com/questions/6456304/scrapy-unit-testing/12741030#12741030]
import os
from scrapy.http import Response, Request


def fake_response_from_file(filename, url=None):

    if not url:
        url = 'http://www.example.com'

    request = Request(url=url)
    if not filename[0] == '/':
        responses_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(responses_dir, filename)
    else:
        file_path = filename

    file_content = open(file_path, 'r').read()

    response = Response(url=url,
                        request=request,
                        body=file_content)
    response.encoding = 'utf-8'
    return response

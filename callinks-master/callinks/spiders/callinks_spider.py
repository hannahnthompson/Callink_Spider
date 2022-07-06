import json 
import scrapy 

class CallinksSpider(scrapy.Spider): 
    name = 'callinks' 
    base_url = 'https://callink.berkeley.edu'
    request_header = '/api/discovery/search/organizations?orderBy%5B0%5D=UpperName%20asc&top=2000&filter=&query=&skip=0'

    def start_requests(self):
        yield scrapy.Request(url=self.base_url + self.request_header, callback=self.parse)

    def parse(self, response): 
        data = json.loads(response.body)
        for item in data.get('value'):
            yield {'website_key': item.get('WebsiteKey')}
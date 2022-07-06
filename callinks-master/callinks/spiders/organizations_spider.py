import json 
import scrapy 

class OrganizationsSpider(scrapy.Spider): 
    name = 'organizations' 
    base_url = 'https://callink.berkeley.edu/organization/'

    def start_requests(self):
        with open('callinks.json') as f:
            orgs = json.load(f)
            for org in orgs:
                yield scrapy.Request(url=self.base_url + org['website_key'], callback=self.parse)

    def parse(self, response): 
        xp = "//script[re:test(text(),'window.initialAppState =','i')]"
        data = response.xpath(xp).re(" = (\{.+\})")[0]
        data = json.loads(data)
        org = data.get('preFetchedData').get('organization')
        yield {'name': org.get('name'),
               'email': org.get('email')}
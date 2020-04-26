# -*- coding: utf-8 -*-
import scrapy
## conda activate virual_workspace

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            # whenever you execute an Xpath expression against a selector object 
            # always start with .// that is the rule
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield {
                'countries_name' : name,
                'countries_link' : link
            }

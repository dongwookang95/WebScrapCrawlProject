# -*- coding: utf-8 -*-
import scrapy
import logging
## conda activate virual_workspace

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            # whenever you execute an Xpath expression against a selector object 
            # always start with .// that is the rule
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            # absolute_url = f"https://www.worldometers.info{link}"
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)
            yield response.follow(url=link, callback = self.parse_country)


    def parse_country(self, response): 
        rows = response.xpath("(//table[@class = 'table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield{
                'year' : year,
                'population' : population
            }

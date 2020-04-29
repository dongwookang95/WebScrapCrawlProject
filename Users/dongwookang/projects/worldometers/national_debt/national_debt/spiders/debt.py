# -*- coding: utf-8 -*-
import scrapy
import logging
## conda activate virual_workspace

class DebtSpider(scrapy.Spider):
    name = 'debt'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']


    def parse(self, response):
        countries = response.xpath("//tbody/tr")
        for country in countries:
            # whenever you execute an Xpath expression against a selector object 
            # always start with .// that is the rule
            name = country.xpath(".//a/text()").get()
            debt = country.xpath(".//td[2]/text()").get()
            # absolute_url = f"https://www.worldometers.info{link}"
            # absolute_url = response.urljoin(link)
            yield {
                'name' : name,
                'debt' : debt
            }
    # def parse_country(self, response): 
    #     name = response.request.meta['country_name']
    #     rows = response.xpath("(//table[@class = 'table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
    #     for row in rows:
    #         year = row.xpath(".//td[1]/text()").get()
    #         population = row.xpath(".//td[2]/strong/text()").get()
    #         yield{
    #             'country_name' :name, 
    #             'year' : year,
    #             'population' : population
    #         }

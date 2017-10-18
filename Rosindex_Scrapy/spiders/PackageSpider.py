# -*- coding: utf-8 -*-
import scrapy
from Rosindex_Scrapy.items import PackageItem
import csv

class PackageSpider(scrapy.Spider):
    name = 'PackageSpider'
    prefix = 'http://rosindex.github.io/p/'
    custom_settings = {
        'ITEM_PIPELINES': {
            'Rosindex_Scrapy.pipelines.DuplicatesPipeline': 300,
            'Rosindex_Scrapy.pipelines.PackageCsvPipeline': 400
        }
    }
    #allowed_domains = ['http://rosindex.github.io/p/agvs_common/']
    #start_urls = ['http://rosindex.github.io/p/agvs_common/']
    # ['http://http://rosindex.github.io/p/agvs_common/', 'http://rosindex.github.io/p/agvs_control/']
    #"""
    def start_requests(self):
        
        prefix = 'http://rosindex.github.io'
        with open('package_links.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                field = ''.join(row).strip("[]'")
                repos_url = prefix + ''.join(field)
                yield scrapy.Request(url=repos_url, callback=self.parse)
    #"""
    def parse(self, response):
        #"""
        Package=PackageItem()
        Package['url']= response.url
        name = set(response.xpath('//li[a/text()="Packages"]/following-sibling::*/text()').extract())
        Package['name'] = ','.join(name)
        repos=response.xpath('//h3/small/a[contains(@href,"/r/")]/text()').extract()
        Package['repository'] = ','.join(set(repos))
        systems = set(response.xpath('//label[contains(@class,"btn-primary")]/@data').extract()\
                  +response.xpath("//li[@class = ' older-distro-option']/@data").extract())
        Package['system_list'] = ','.join(systems)
        denpendenyset=response.xpath('//div[h3/text()="Package Dependencies"]'
                                     '/following-sibling::*'
                                     '//td[not(@class)]/a[contains(@href,"/p/")]/text()').extract()
        dependency=list(set(denpendenyset))
        dependency.sort(key=denpendenyset.index)
        Package['dependency_packages']=','.join(dependency)
        denpendentset=response.xpath('//div[h3/text()="Dependant Packages"]'
                                     '/following-sibling::*'
                                     '//td[not(@class)]/a[contains(@href,"/p/")]/text()').extract()
        dependent=list(set(denpendentset))
        dependent.sort(key=denpendentset.index)
        Package['dependant_packages']=','.join(dependent)
        readmeset=response.xpath('//div[text()=" README"]/following-sibling::*').extract()
        Package['readme'] = ','.join(set(readmeset)).strip('{}').encode('utf-8')
        #print(Package)
        yield Package
        #"""
        #print('package page is parsed...')

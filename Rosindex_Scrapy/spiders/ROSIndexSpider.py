# -*- coding: utf-8 -*-
import scrapy
import csv
#import Rosindex_Scrapy.items
from Rosindex_Scrapy.items import RepositoryItem,PackageItem,ROS_systemItem

class RosindexspiderSpider(scrapy.Spider):
    name = 'ROSIndexSpider'
    #allowed_domains = ['http://rosindex.github.io']
    start_urls = ['http://rosindex.github.io/packages/page/1/time/']

    #def parse(self, response):
     #   pass

    def parse(self, response):
        print('one repos page  parsed')
        repository=RepositoryItem()
        links=response.xpath('//td/a[contains(@href,"/p/")]')
        for link in links:
            repository['url']=link.xpath('@href').extract()
            #repository['name']=link.xpath('text()').extract()
            #print(repository['url'])
            #print(repository['name'])
            yield repository

        """" 
        with open('repos_links.csv', 'w') as csvfile:
            writer= csv.writer(csvfile)
            #writer.writerow(['repository name','url'])
            for link in repos_links[0:50]:
                #repository['name'] = link.xpath('/text()').extract()
                repository['url'] = link.extract()
                print(repository['url'])
                writer.writerow([format(repository['url'])])
        """

        next_page=response.xpath('//li/a[contains(text(), "»")]/@href').extract()
        if next_page[0]!='#':
            yield scrapy.Request('http://rosindex.github.io'+next_page[0], callback=self.parse)

        """" 
        package_links=response.xpath('//div[1]/td/a[contains(@href,"/p/")]/@href').extract()
        print('packages links:')
        print(package_links)
        for link in package_links:
            yield scrapy.Request('http://rosindex.github.io'+link, callback=self.parse_package)
        """
    def parse_next(self, response):
        print('next page is parsed...')




    def parse_package(self, response):
        package=PackageItem()
        package['name']=response.xpath('//h3/a[contains(@href,"/p/")]/text()').extract()
        print('one package page is parsed, the package name is:')
        print(package['name'])



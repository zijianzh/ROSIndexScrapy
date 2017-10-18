# -*- coding: utf-8 -*-
import scrapy
from Rosindex_Scrapy.items import RepositoryItem
import csv


class RepositorySpider(scrapy.Spider):
    name = 'RepositorySpider'
    #allowed_domains = ['http://rosindex.github.io/r/agvs_common/']
    #start_urls = ['http://rosindex.github.io/r/iai_common_msgs/']
    prefix = 'http://rosindex.github.io/r/'
    custom_settings = {
        'ITEM_PIPELINES': {
            'Rosindex_Scrapy.pipelines.DuplicatesPipeline': 300,
            'Rosindex_Scrapy.pipelines.ReposCsvPipeline':400
            #'Rosindex_Scrapy.pipelines.ReposRestCsvPipeline':400
        }
    }


    def start_requests(self):
        #""""
        prefix = 'http://rosindex.github.io'
        with open('repos_links.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                field = ''.join(row).strip("[]'")
                repos_url = prefix + ''.join(field)
                yield scrapy.Request(url=repos_url, callback=self.parse)
        #"""
        #yield scrapy.Request(url='http://rosindex.github.io/r/iai_common_msgs/', callback=self.parse)


    def parse(self, response):
        Repository = RepositoryItem()
        Repository['url'] = response.url
        name = set(response.xpath('//li[a/text()="Repos"]/following-sibling::*/text()').extract())
        Repository['name'] = ','.join(name)
        packageset = response.xpath('//td/a[contains(@href,"/p/")]/text()').extract()
        packages= list(set(packageset))
        packages.sort(key=packageset.index)
        Repository['package_list']=','.join(packages)
        systems = set(response.xpath('//label[contains(@class,"btn-primary")]/@data').extract()\
                                    +response.xpath("//li[@class = ' older-distro-option']/@data").extract())
        Repository['system_list']=','.join(systems)
        Repository['readme'] = set(response.xpath('//div[h3/text()="README"]/following-sibling::*').extract())
        #Repository['readme'] = ''.join(readme).encode('utf-8')
        #Repository['readme'].sort(key=readme.index)
        #print(Repository)
        yield Repository
        #if response.url != 'http://rosindex.github.io/r/agvs_common/':
            #yield scrapy.Request('http://rosindex.github.io/r/agvs_common/', callback=self.parse)

    def parse_test(self, response):
        print(response.url+' is parsed...')

# -*- coding: utf-8 -*-
import scrapy
from Rosindex_Scrapy.items import RepositoryItem

class RepositorySpider(scrapy.Spider):
    name = 'RepositorySpider'
    #allowed_domains = ['http://rosindex.github.io/r/agvs_common/']
    start_urls = ['http://rosindex.github.io/r/rtmros_common/#kinetic']
    prefix = 'http://rosindex.github.io/r/'

    def parse(self, response):
        Repository = RepositoryItem()
        Repository['url'] = response.url
        Repository['name'] = Repository['url'].lstrip(self.prefix)
        Repository['name'].strip('/')
        packages = response.xpath('//td/a[contains(@href,"/p/")]/@href').extract()
        Repository['package_list'] = list(set(packages))
        Repository['package_list'].sort(key=packages.index)
        older_systems = response.xpath("//li[@class = ' older-distro-option']/@data").extract()
        Repository['system_list'] = response.xpath('//label[contains(@class,"btn-primary")]/@data').extract()+older_systems
        readme = response.xpath('//div[h3/text()="README"]/following-sibling::*').extract()
        Repository['readme'] = list(set(readme))
        Repository['readme'].sort(key=readme.index)
        print(Repository)


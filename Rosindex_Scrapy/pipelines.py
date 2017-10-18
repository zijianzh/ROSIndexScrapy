# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class RosindexScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class DuplicatesPipeline(object):

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        print('DuplicatesPipeline...')
        if format(item['url']) in self.urls_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.urls_seen.add(format(item['url']))
            return item
"""
import csv
class CSVPipeline(object):
    def __init__(self):
        self.file = open('items.csv', 'w')
    def process_item(self, item, spider):
        line = csv.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
"""

import csv
#from Rosindex_Scrapy import settings

#   def write_to_csv(item):
#      writer = csv.writer(open(settin.csv_file_path, 'a'), lineterminator='\n')
#       writer.writerow([item[key] for key in item.keys()])

class UrlsToCsv(object):
    def __init__(self):
        self.csvfile = open('package_links.csv', 'a+')

    def process_item(self, item, spider):
        print('UrlsToCsv pipeline...')
        writer = csv.writer(self.csvfile)
        writer.writerow([format(item['url'])])

    def spider_closed(self, spider):
        self.csvfile.close()


from scrapy.exporters import CsvItemExporter
class CsvPipeline(object):
    def __init__(self):
        self.file = open("repos_items.csv", 'a+')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        print('CsvPipeline...')
        self.exporter.export_item(item)
        return item

class ReposCsvPipeline(object):
    def __init__(self):
        self.repos_fields = ['name', 'url', 'system list', 'package list', 'readme']
        self.csvfile = open('repos_items.csv', 'a+')
        writer = csv.DictWriter(self.csvfile, fieldnames=self.repos_fields)
        writer.writeheader()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        print('ReposCsvPipeline...')
        writer = csv.DictWriter(self.csvfile, fieldnames=self.repos_fields)
        readme = ''.join(item['readme'])
        README = readme.encode('utf-8')
        writer.writerow({'name': item['name'],
                         'url': item['url'],
                         'system list': item['system_list'],
                         'package list': item['package_list'],
                         'readme': README})

    def close_spider(self, spider):
        self.csvfile.close()

class ReposRestCsvPipeline(object):
    def __init__(self):
        self.repos_fields = ['name',
                             'url',
                             'system list',
                             'package list',
                             'readme']
        self.csvfile = open('repos_rest_items.csv', 'a+')
        writer = csv.DictWriter(self.csvfile, fieldnames=self.repos_fields)
        writer.writeheader()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        print('ReposCsvPipeline...')
        writer = csv.DictWriter(self.csvfile, fieldnames=self.repos_fields)
        readme = ''.join(item['readme'])
        README=readme.encode('utf-8')
        writer.writerow({'name': item['name'],
                         'url': item['url'],
                         'system list': item['system_list'],
                         'package list': item['package_list'],
                         'readme': README})

    def close_spider(self, spider):
        self.csvfile.close()

class PackageCsvPipeline(object):
    def __init__(self):
        self.repos_fields = ['name',
                             'url',
                             'system list',
                             'repository',
                             'dependency packages',
                             'dependant packages',
                             'readme']
        self.csvfile = open('package_items.csv', 'a+')
        writer = csv.DictWriter(self.csvfile, fieldnames=self.repos_fields)
        writer.writeheader()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        print('PackageCsvPipeline...')
        writer = csv.DictWriter(self.csvfile, fieldnames=self.repos_fields)
        #readme = ''.join(item['readme'])
        #README = readme.encode('utf-8')
        writer.writerow({'name': ''.join(item['name']),
                         'url': item['url'],
                         'system list': item['system_list'],
                         'dependency packages': item['dependency_packages'],
                         'dependant packages': item['dependant_packages'],
                         'readme': item['readme']})

    def close_spider(self, spider):
        self.csvfile.close()
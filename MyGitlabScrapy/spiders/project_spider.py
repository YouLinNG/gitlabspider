# -*- coding: utf-8 -*-
import scrapy
from MyGitlabScrapy.items import ProjectItem
from scrapy import Request
import json

class ProjectSpiderSpider(scrapy.Spider):
    name = 'project_spider'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        start_urls = []
        file = open("MyGitlabScrapy/spiders/gitlabweb.json", "rb")
        data = json.load(file)
        for item in data:
            start_urls.append(item["project_hash"])

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        project = ProjectItem()

        project['project_id'] = response.xpath('//span[@class="text-secondary"]/text()').extract()
        project['project_commit'] = response.xpath('//ul[@class="nav"]/li[2]/a/strong[@class="project-stat-value"]/text()').extract()
        project['project_branch'] = response.xpath('//ul[@class="nav"]/li[3]/a/strong[@class="project-stat-value"]/text()').extract()
        project['project_size'] = response.xpath('//ul[@class="nav"]/li[5]/a/strong[@class="project-stat-value"]/text()').extract()
        project['project_star'] = response.xpath('//span[@class="star-count count-badge-count d-flex align-items-center"]/text()').extract()

        yield project

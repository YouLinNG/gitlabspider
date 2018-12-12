# -*- coding: utf-8 -*-
import scrapy
from MyGitlabScrapy.items import ProjectItem

class ProjectSpiderSpider(scrapy.Spider):
    name = 'project_spider'
    allowed_domains = ['https://gitlab.com/fdroid/fdroidclient']
    start_urls = ['http://https://gitlab.com/fdroid/fdroidclient/']

    def parse(self, response):

        project = ProjectItem()

        project['project_id'] = response.xpath('//div[@class="text-secondary prepend-top-8"]').extract()

        print(project)

        pass

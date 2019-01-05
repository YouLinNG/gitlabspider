import scrapy
from MyGitlabScrapy.items import ProjectCommitItem
import sys

class MySpider(scrapy.Spider):
    name = 'project_commit'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    start_urls = ["https://gitlab.com/fdroid/fdroidclient/commits/master", ]

    def parse(self, response):
        project_commit = ProjectCommitItem()

        project_commit['commit_href'] = response.xpath('//div[@class="d-block d-sm-none"]/a/@href').extract()
        project_commit['build_result'] = response.xpath('//div[@class="d-block d-sm-none"]/a/@title').extract()
        yield project_commit
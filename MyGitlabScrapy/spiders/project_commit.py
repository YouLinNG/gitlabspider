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

        project_commit['commit_id'] = response.xpath( '//div[@class="label label-monospace"]/text()').extract()
        # commit_href is empty
        # project_commit['commit_href'] = response.xpath('//a[@class="commit-row-message item-title"]/@href').extract()
        project_commit['build_result'] = response.xpath('//li[@class="commits-row"]/ul/li[@class="commit flex-row js-toggle-container"]/div[@class="commit-detail flex-list"]/div[@class="commit-actions flex-row d-none d-sm-flex"]/a/@data-original-title').extract()

        yield project_commit
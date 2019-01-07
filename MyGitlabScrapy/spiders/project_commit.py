import scrapy
from MyGitlabScrapy.items import ProjectCommitItem
import sys

class MySpider(scrapy.Spider):
    name = 'project_commit'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    baseURL = 'https://gitlab.com/fdroid/fdroidclient/commits/master';
    URLstr = '?limit=40&offset=';
    offset = 40;
    start_urls = [baseURL,baseURL + URLstr + str(offset)];

    def parse(self, response):
        project_commit = ProjectCommitItem()

        project_commits = response.xpath('//div[@class="d-block d-sm-none"]')

        for commit in project_commits:
            project_commit['commit_href'] = commit.xpath('.//a/@href').extract()[0]
            project_commit['build_result'] = commit.xpath('.//a/@title').extract()[0]
            yield project_commit

        if self.offset<400:
            self.offset+=40
            url=self.baseURL+ self.URLstr + str(self.offset)
            yield scrapy.Request(url,callback=self.parse)
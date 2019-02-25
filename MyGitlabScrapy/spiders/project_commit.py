import scrapy
from MyGitlabScrapy.items import ProjectCommitItem
import sys
import re

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

        project_commits = response.xpath('//li[@class="commit flex-row js-toggle-container"]')

        for commit in project_commits:
            p1 = re.compile('.*Commit: .*')
            project_commit['commit_href'] = "https://gitlab.com" + commit.xpath('.//div[@class="commit-detail flex-list"]/div[@class ="commit-content qa-commit-content"]/a/@href').extract()[0]
            build_result_exist= commit.xpath('.//div[@class="commit-detail flex-list"]/div[@class ="commit-content qa-commit-content"]').extract()[0]
            exist_or_not = re.search(p1, build_result_exist)
            if exist_or_not:
                project_commit['build_result']= commit.xpath('.//div[@class="commit-detail flex-list"]/div[@class ="commit-content qa-commit-content"]/div[@class ="d-block d-sm-none"]/a/@title').extract()[0]
            else:
                project_commit['build_result']= ""
            yield project_commit


        if True:
            self.offset+=40
            url=self.baseURL+ self.URLstr + str(self.offset)
            yield scrapy.Request(url,callback=self.parse)
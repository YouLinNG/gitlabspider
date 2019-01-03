import scrapy
from MyGitlabScrapy.items import CommitInfoItem
import sys

class MySpider(scrapy.Spider):
    name = 'commit_info'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    start_urls = ["https://gitlab.com/fdroid/fdroidclient/commit/823ddcaca8fe98a0254a224a8aefdb30c42e305b", ]

    def parse(self, response):
        commit_info = CommitInfoItem()

        commit_info['commit_id'] = response.xpath( '//div[@class="header-main-content"]/strong/span[@class="commit-sha"]/text()').extract()
        # commit_info['commit_time'] = response.xpath('//div[@class="header-main-content"]/time[@class="js-timeago js-timeago-render"]/@datetime').extract()
        commit_info['author_name'] = response.xpath('//span[@class="commit-author-name"]/text()').extract()

        commit_info['commit_title'] = response.xpath('//h3[@class="commit-title"]/text()').extract()
        commit_info['commit_description'] = response.xpath('//pre[@class="commit-description"]/text()').extract()

        commit_info['changed_file_num'] = response.xpath('//button[@class="diff-stats-summary-toggler js-diff-stats-dropdown"]/text()').extract()
        commit_info['changed_file'] = response.xpath( '//div[@class="file-header-content"]/a/strong[@class="file-title-name has-tooltip"]/text()').extract()

        commit_info['additions_num'] = response.xpath('//span[@class="diff-stats-additions-deletions-expanded"]/strong[@class="cgreen"]/text()').extract()
        commit_info['deletions_num'] = response.xpath('//span[@class="diff-stats-additions-deletions-expanded"]/strong[@class="cred"]/text()').extract()
        yield commit_info
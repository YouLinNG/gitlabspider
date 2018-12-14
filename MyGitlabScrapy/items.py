# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 项目ID
    project_id = scrapy.Field()

    # 项目大小
    project_size = scrapy.Field()

    # 项目star
    project_star = scrapy.Field()

    # 项目commit
    project_commit = scrapy.Field()

    # 项目branch数
    project_branch = scrapy.Field()
    pass


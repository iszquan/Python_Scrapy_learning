from typing import Iterable

import scrapy
from scrapy import Request
from ..items import MovieItem


class Ssr1Spider(scrapy.Spider):
    name = "ssr1"
    allowed_domains = ["ssr1.scrape.center"]
    base_url = "https://ssr1.scrape.center"
    MAX_PAGE = 10

    def start_requests(self):
        for page in range(1, self.MAX_PAGE+1):
            url = f'{self.base_url}/page/{page}'
            yield Request(url, callback=self.parse_index)

    def parse_index(self, response):
        for item in response.css('.item'):
            href = item.css('.name::attr(href)').extract_first()
            detail_url = response.urljoin(href)
            yield Request(detail_url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = MovieItem()
        item['name'] = response.xpath('//div[contains(@class, "item")]//h2/text()').extract_first()
        item['categories'] = response.xpath('//button[contains(@class, "category")]/span/text()').extract()
        item['score'] = response.css('.score::text').re_first('[\d\.]+')
        item['drama'] = response.css('.drama p::text').extract_first().strip()
        item['directors'] = []
        directors = response.xpath('//div[contains(@class, "directors")]//div[contains(@class, "director")]')
        for director in directors:
            director_image = director.xpath('.//img[@class="image"]/@src').extract_first()
            director_name = director.xpath('.//p[contains(@class, "name")]/text()').extract_first()
            item['directors'].append({
                'name': director_name,
                'image': director_image
            })
        item['actors'] = []
        actors = response.css('.actors .actor')
        for actor in actors:
            actor_name = actor.css('.actor .name::text').extract_first()
            actor_image = actor.css('.actor .image::attr(src)').extract_first()
            item['actors'].append({
                'name': actor_name,
                'image': actor_image
            })
        yield item

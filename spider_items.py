import json
from typing import List

import scrapy

import config
from utils import uri


def get_urls(search: str) -> List[str]:
    url = config.URL
    urls = []

    pages = 1
    with open('pages.json', 'r') as f:
        try:
            pages = json.load(f)[0]['pages']
        except json.decoder.JSONDecodeError as e:
            print(f'Error: {e}')

    for i in range(1, pages+1):
        params = {
            config.SEARCH_PARAM: search,
            config.PAGE_PARAM: i
        }
        url = uri.get_uri(url, params)
        urls.append(url)
    return urls


class AvitoItemsSpider(scrapy.Spider):
    name = 'avitoitemsspider'

    def __init__(self, search='', *args, **kwargs):
        self.start_urls = get_urls(search)
        super(AvitoItemsSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        gallery = response.css('div.iva-item-root-G3n7v')

        for item in gallery:
            title = item.css('h3::text')
            price = item.css('span.price-root-1n2wM>span>span::text')
            geo = item.css('div.geo-root-1pUZ8>span>span::text')
            data = {
                'title': title.get(),
                'price': price.get(),
                'geo': geo.get()
            }
            yield data

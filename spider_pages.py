import scrapy

import config


def get_url(search: str) -> str:
    url = f'{config.URL}{config.SEARCH_PARAM}={search}'
    return url


class AvitoPagesSpider(scrapy.Spider):
    name = 'avitopagesspider'

    def __init__(self, search='', *args, **kwargs):
        self.start_urls = [get_url(search)]
        super(AvitoPagesSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        buttons = response.css('span.pagination-item-1WyVp::text')
        pages = 1
        for button in buttons:
            text = button.get()
            if text.isdigit():
                pages = int(text)
        yield {
            'pages': pages
        }

import scrapy

class rostrumSpider(scrapy.Spider):
    name = "titles"
    start_urls = [
            'https://www.rostrum.blog/2019/09/20/say-package/',
            'https://www.rostrum.blog/2019/09/12/live-code/',
        ]

    def parse(self, response):
        for wrapper in response.css('div.wrapper'):
            yield {
                'title': response.css('title::text').get(),
                'h1': response.css('h1::text').getall(),
            }
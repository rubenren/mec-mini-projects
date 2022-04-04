# xpath_spider
import scrapy

class XpathSpider(scrapy.Spider):
    name = "toscrape-xpath"

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath('//*[@class="quote"]'):
            yield {
                'text': quote.xpath('span[@itemprop="text"]/text()').get(),
                'author': quote.xpath('span/*[@itemprop="author"]/text()').get(),
                'tags': quote.xpath('div/a/text()').getall()
            }
        yield from response.follow_all(css='ul.pager a', callback=self.parse)
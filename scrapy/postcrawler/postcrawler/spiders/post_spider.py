import scrapy

class PostsSpider(scrapy.Spider):
    name="news"

    start_urls = [
        "https://www.marketpulse.com/news-events"
    ]

    def parse(self, response):
        filename = 'eurusd-news.html'

        with open(filename, 'wb') as f:
            f.write(response.body)
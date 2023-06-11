import scrapy

class PostsSpider(scrapy.Spider):
    name="news"

    start_urls = [
        "https://www.marketpulse.com/news-events"
    ]

    def parse(self, response):
        filename = 'fx-news.html'
        sections = response.css('div.awyw')
        page_content = ''
        for sect in sections:
            sect_main = f"<h1>{sect.css('div.wa-head h5::text').get()}<h1>"
            sect_news = sect.css('div.wa-body').css('div.clear h6 a')
            sect_links = sect_news.xpath('@href').extract()
            sect_headings = sect_news.xpath('text()').extract()
            sect_times = sect.css('div.wa-body').css('div.clear time::text').getall()
            page_content += sect_main

            for i in range(len(sect_headings)):
                entry = f"<a href='{sect_links[i]}'>{sect_headings[i]} POSTED AT {sect_times[i]}</a><br>"
                page_content += entry 


        with open(filename, 'w') as f:
            f.write(page_content)
import scrapy

class medscraper(scrapy.Spider):
    name = "alicia"

    def start_requests(self):
        list_of_urls = ["https://medium.com/",
                        "https://medium.com/@appiahyoofi/goodbye-node-js-9e2f71f5e430",
                        "https://medium.com/@developinggamer/how-i-made-my-github-profile-stand-out-d2d2bf6e98c7"
                        ]
        for url in list_of_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.css("img::attr(src)").extract())
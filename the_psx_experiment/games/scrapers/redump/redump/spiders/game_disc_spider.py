import scrapy

class GameDiscSpider(scrapy.Spider):
    name = 'game_discs'

    def start_requests(self):
        urls = ['http://redump.org/discs/system/psx/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_list)
    
    def parse_list(self, response):
        game_links = response.xpath('//div[@class="gamesblock"]/table/tr/td/a/@href').getall()

        for game_link in game_links:
            yield response.follow(game_link, self.parse_game)
    
    def parse_game(self, response):
        titles = []
        game_div = response.xpath('//div[@id="main"]')
        titles.append(game_div.xpath('//h1/text()').get())
        titles.append(game_div.xpath('//h2/text()').get())
        print(titles)

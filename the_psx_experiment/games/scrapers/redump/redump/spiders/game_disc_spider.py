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

        gameinfo_table_rows = response.xpath('//table[@class="gameinfo"]/tr')

        for row in gameinfo_table_rows:
            header = row.xpath('.//th/text()').get()
            if header == 'Region':
                region = row.xpath('.//td/a/img/@title').get()
                print(region)
            if header == 'Serial':
                serials = row.xpath('.//td/text()').get()
                serials = serials.split(',')
                serials = [serial.strip() for serial in serials]
                print(serials)
            if header == 'EXE date':
                exe_date = row.xpath('.//td/text()').get()
                print(exe_date)
            if header == 'Edition':
                editions = row.xpath('.//td/text()').get()
                editions = editions.split(',')
                editions = [edition.strip() for edition in editions]
                print(editions)

import scrapy

class GameDiscSpider(scrapy.Spider):
    name = 'game_discs'
    BASE_URL = "http://redump.org"

    def start_requests(self):
        urls = [f'{self.BASE_URL}/discs/system/psx/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_list)

    def parse_list(self, response):
        game_links = response.xpath('//div[@class="gamesblock"]/table/tr/td/a/@href').getall()

        for game_link in game_links:
            yield response.follow(game_link, self.parse_game_disc)

        next_link = response.xpath('//div[@class="pages"]/ul/li/a[text()=">>"]/@href').get()
        next_link = f'{self.BASE_URL}{next_link}'
        if next_link:
            yield scrapy.Request(url=next_link, callback=self.parse_list)

    def parse_game_disc(self, response):
        titles = []
        region = 'Unknown'
        serials = ['Unknown']
        editions = ['Unknown']
        exe_date = '1900-01-01'

        game_div = response.xpath('//div[@id="main"]')
        titles.append(game_div.xpath('//h1/text()').get())
        titles.append(game_div.xpath('//h2/text()').get())

        gameinfo_table_rows = response.xpath('//table[@class="gameinfo"]/tr')

        for row in gameinfo_table_rows:
            header = row.xpath('.//th/text()').get()
            if header == 'Region':
                region = row.xpath('.//td/a/img/@title').get()
            if header == 'Serial':
                serials = row.xpath('.//td/text()').get()
                serials = serials.split(',')
                serials = [serial.strip() for serial in serials]
            if header == 'EXE date':
                exe_date = row.xpath('.//td/text()').get()
            if header == 'Edition':
                editions = row.xpath('.//td/text()').get()
                editions = editions.split(',')
                editions = [edition.strip() for edition in editions]
        discs = zip(serials, editions)
        for disc in discs:
            yield {
                'title_1': titles[0],
                'title_2': titles[1],
                'region': region,
                'exe_date': exe_date,
                'serial': disc[0],
                'edition': disc[1]
            }

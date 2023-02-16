import scrapy

class GameReleaseSpider(scrapy.Spider):
    name = "game_releases"

    def start_requests(self):
        self.page = 1
        self.last_page = 40
        url = f"https://www.satakore.com/sega-saturn-complete-game,,{self.page},,0,,1.html"
        yield scrapy.Request(url=url, callback=self.parse_list)

    def parse_list(self, response):
        game_table = response.xpath('//table[@class="table_search"]')
        rows = game_table.xpath(".//tr")
        for row in rows:
            game_link = row.xpath('.//td[@class="tdleft"]/a/@href').get()
            if game_link:
                yield response.follow(game_link, self.parse_game)

        self.page += 1
        if self.page <= self.last_page:
            yield scrapy.Request(url=f"https://www.satakore.com/sega-saturn-complete-game,,{self.page},,0,,1.html", callback=self.parse_list)

    def parse_game(self, response):
        game_div = response.xpath('//div[@id="satengine"]')
        title = "Unknown"
        title = game_div.xpath('//h1[@class="gametitle"]/text()').get()
        title_2 = "Unknown"
        title_2 = game_div.xpath('//h2[@class="tshad1"]/text()').get()
        serial_number = "Unknown"
        serial_number = game_div.xpath("//h3/text()").get()
        region = "Unknown"
        release_date = "Unknown"
        developer = "Unknown"
        publisher = "Unknown"

        coredata_divs = response.xpath('//div[@class="coredata-data1-data"]')
        for div in coredata_divs:
            header = div.xpath('//span[@class="bold"]/text()').get()
            if header == "Region:":
                region = div.xpath("//text").get()
            if header == "Release Date:":
                release_date = div.xpath("//text()").get()
            if header == "Developer:":
                developer = div.xpath("//text()").get()
            if header == "Publisher:":
                publisher = div.xpath("//text()").get()

        yield {
            "Title 1": title,
            "Title 2": title_2,
            "Serial #": serial_number,
            "Region": region,
            "Release Date": release_date,
            "Developer": developer,
            "Publisher": publisher
        }
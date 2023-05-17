import scrapy

class GameReleaseSpider(scrapy.Spider):
    name = "game_releases"

    attribute_map = {
        'Game Identification': {
            'Official Title': 'official_title',
            'Common Title': 'common_title',
            'Serial Number(s)': 'serial_numbers',
            'Region': 'region',
            'Genre / Style': 'genre_style',
            'Developer': 'developer',
            'Publisher': 'publisher',
            'Date Released': 'date_released'
        }
    }

    def start_requests(self):
        urls = [
            'https://psxdatacenter.com/jlist.html',
            'https://psxdatacenter.com/ulist.html',
            'https://psxdatacenter.com/plist.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_list)

    def parse_list(self, response):
        game_tables = response.xpath('//table[@class="sectiontable"]')
        for table in game_tables:
            rows = table.xpath('.//tr')
            for row in rows:
                game_link = row.xpath('.//td[@class="col1"]/a/@href').get()
                if game_link:
                    yield response.follow(game_link, self.parse_game)

    def parse_game(self, response):
        parsed_game = {
            'disc_serial_numbers': []
        }

        game_id_table = response.xpath('//table[@id="table4"]')
        game_id_table_rows = game_id_table.xpath('.//tr')
        for row in game_id_table_rows:
            row_cells = row.xpath('.//td/text()').getall()
            row_cells = [cell.strip() for cell in row_cells]
            if self.attribute_map['Game Identification'].get(row_cells[0]):
                attribute_name = self.attribute_map['Game Identification'][row_cells[0]]
                parsed_game[attribute_name] = row_cells[1]

        disc_info_table = response.xpath('//table[@id="table7"]')
        disc_info_table_rows = disc_info_table.xpath('.//tr')
        for row in disc_info_table_rows:
            row_cells = row.xpath('.//td/text()').getall()
            row_cells = [cell.strip() for cell in row_cells]
            if row_cells[0] == 'Serial Number In Disc':
                for cell in row_cells[1:]:
                    parsed_game['disc_serial_numbers'].append(cell)

        yield parsed_game

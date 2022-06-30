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
        },
        'Game Features': {
            'Number Of Players': 'number_of_players',
            'Number Of Memory Card Blocks': 'memory_card_blocks',
            'Compatible Controllers Tested': 'compatible_controllers',
            'Compatible Light Guns': 'compatible_light_guns',
            'Other Compatible Controllers': 'other_compatible_controllers',
            'Special Controllers Included Or': 'special_controllers',
            'Vibration Function Compatible': 'vibration',
            'Multi-Tap Function Compatible': 'multitap',
            'Link Cable Function Compatibile': 'link_cable'
        },
        'Emulation': {
            'Emulator': 'emulator',
            'Video Plugin': 'video_plugin',
            'Audio Plugin': 'audio_plugin',
            'CD-ROM Plugin': 'cdrom_plugin',
            'Game Pad Plugin': 'gamepad_plugin',
            'Vibration Compatible': 'vibration',
            'Console Bios Used': 'console_bios'
        }
    }

    extra_fields = [
        'Compatible Controllers Tested',
        'Compatible Light Guns',
        'Other Compatible Controllers',
        'Special Controllers Included Or'
    ]

    def start_requests(self):
        urls = [
            'https://psxdatacenter.com/jlist.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_list)

    def parse_list(self, response):
        game_tables = response.css('table.sectiontable')
        for table in game_tables[0:1]:
            rows = table.xpath('.//tr')
            for row in rows[0:5]:
                game_link = row.css('td.col1').xpath('.//a/@href').get()
                if game_link:
                    yield response.follow(game_link, self.parse_game)

    def parse_game(self, response):
        parsed_game = {
            'game_features': {},
            'emulation': {}
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

        languages_table = response.xpath('//table[@id="table13"]')

        text_block_tables = response.xpath('//table[@id="table16"]')
        text_blocks = text_block_tables.xpath('.//td').getall()
        parsed_game['game_description'] = text_blocks[0].strip()
        parsed_game['game_controls'] = text_blocks[1].strip()
        parsed_game['game_cheats'] = text_blocks[2].strip()

        game_features_table = response.xpath('//table[@id="table19"]')
        game_features_rows = game_features_table.xpath('.//tr')
        for row in game_features_rows:
            row_cells = row.xpath('.//td/text()').getall()
            row_cells = [cell.strip() for cell in row_cells]
            if self.attribute_map['Game Features'].get(row_cells[0]):
                attribute_name = self.attribute_map['Game Features'][row_cells[0]]
                if row_cells[0] in self.extra_fields:
                    parsed_game['game_features'][attribute_name] = row_cells[2]
                else:
                    parsed_game['game_features'][attribute_name] = row_cells[1]

        emulation_table = response.xpath('//table[@id="table25"]')
        emulation_rows = emulation_table.xpath('.//tr')
        for row in emulation_rows:
            row_cells = row.xpath('.//td/text()').getall()
            row_cells = [cell.strip() for cell in row_cells]
            if self.attribute_map['Emulation'].get(row_cells[0]):
                attribute_name = self.attribute_map['Emulation'][row_cells[0]]
                parsed_game['emulation'][attribute_name] = row_cells[1]

        yield parsed_game

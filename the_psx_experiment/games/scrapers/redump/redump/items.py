# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoIte
from games.models import GameDisc


class GameDiscItem(scrapy.Item):
    django_model = GameDisc

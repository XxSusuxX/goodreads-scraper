# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join

def tira_espacos(text):
    return text.strip()

def processa_caracteres(text):
    return text.replace(u"\u2019", '')

def letra_maiuscula(text):
    return text.upper()

class CitacaoItem(scrapy.Item):
    frase = scrapy.Field(
        input_processor=MapCompose(tira_espacos, processa_caracteres),
        output_processor=TakeFirst()
    )
    autor = scrapy.Field(
        input_processor=MapCompose(tira_espacos, letra_maiuscula),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(';')
    )

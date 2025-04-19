import scrapy  # type: ignore
from scrapy.loader import ItemLoader
from varredor_de_sites.items import CitacaoItem

class GoodReadsSpider(scrapy.Spider):
    # Identidade
    name = 'goodreads'

    # Construtor para inicializar as variáveis
    def __init__(self, max_pages=1, *args, **kwargs):
        super(GoodReadsSpider, self).__init__(*args, **kwargs)
        self.max_pages = int(max_pages)  # Número máximo de páginas a serem extraídas
        self.page_count = 0  # Contador de páginas já processadas

    # Request
    def start_requests(self):
        urls = ['https://www.goodreads.com/quotes']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        for elemento in response.xpath('//div[@class="quote"]'):
            loader = ItemLoader(item=CitacaoItem(), selector=elemento, response=response)
            loader.add_xpath('frase', './/div[@class="quoteText"]/text()')
            loader.add_xpath('autor', './/span[@class="authorOrTitle"]/text()')
            loader.add_xpath('tags', './/a[starts-with(@href, "/quotes/tag")]/text()')
            yield loader.load_item()

        # Varrer mais páginas
        if self.page_count < self.max_pages:
            try:
                link_next_page = response.xpath("//a[@class='next_page']/@href").get()
                if link_next_page:
                    self.page_count += 1
                    yield response.follow(link_next_page, callback=self.parse)
            except Exception as e:
                self.logger.info(f"Não há mais páginas: {e}")
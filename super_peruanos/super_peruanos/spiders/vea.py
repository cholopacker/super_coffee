import scrapy   

class MetroCoffeeSpider(scrapy.Spider):
    name = 'vea_coffee'
    start_urls = [
        'https://www.plazavea.com.pe/desayunos/cafe-e-infusiones/cafe-molido-y-granos'
    ]

    custom_settings = {
        'FEED_URI': 'vea_coffee.json',
        'FEED_FORMAT': 'json',   #Para crear archivo json directamente sin necesidad de indicar en consola
        'CONCURRENT_REQUESTS': 48,  #Establece un entero para hacer n repeticiones a la vez
        'MEMUSAGE_LIMIT_MB': 2048,   #Establece cuánta RAM se puede usar
        'MEMUSAGE_NOTIFY_MAIL': ['saul.mendoza.lizana@gmail.com'],   #Notifica cuando se llega al límite de RAM
        'ROBOTSTXT_OBEY': True,  #Para obedecer el robots.txt
        'USER_AGENT': 'JuanchoTacorta',  #Para indicar usuario al servidor
        'FEED_EXPORT_ENCODING': 'utf-8' #Para no tener caracteres raros
    }
   
    
    item_name = '//a[@itemprop="name"]/text()'
    #regular_price = '//div[@class="Showcase__oldPrice Showcase__oldPrice"]/text()'  #does not append empty names
    #regular_price might not exist sometimes
    online_price = '//div[@class="Showcase__salePrice"]/text()'
        

    def parse(self, response):
        item_name = response.xpath(self.item_name).getall()
        #regular_price = response.xpath(self.regular_price).getall()
        online_price = response.xpath(self.online_price).getall()
        

        yield{
            'items': list(zip(item_name, online_price))
            #'item_name': item_name,
            #'brand': brand,
            #'regular_price': regular_price,
            #'online_price': online_price,
            #'link': link
        }
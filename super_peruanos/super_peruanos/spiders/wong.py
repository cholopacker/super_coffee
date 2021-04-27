import scrapy   

class WongCoffeeSpider(scrapy.Spider):
    name = 'wong_coffee'
    start_urls = [
        'https://www.wong.pe/desayuno/cafe-e-infusiones/cafe-molido-y-granos'
    ]

    custom_settings = {
        'FEED_URI': 'wong_coffee.json',
        'FEED_FORMAT': 'json',   #Para crear archivo json directamente sin necesidad de indicar en consola
        'CONCURRENT_REQUESTS': 48,  #Establece un entero para hacer n repeticiones a la vez
        'MEMUSAGE_LIMIT_MB': 2048,   #Establece cuánta RAM se puede usar
        'MEMUSAGE_NOTIFY_MAIL': ['saul.mendoza.lizana@gmail.com'],   #Notifica cuando se llega al límite de RAM
        'ROBOTSTXT_OBEY': True,  #Para obedecer el robots.txt
        'USER_AGENT': 'JuanchoTacorta',  #Para indicar usuario al servidor
        'FEED_EXPORT_ENCODING': 'utf-8' #Para no tener caracteres raros
    }
   
    
    item_name = '//a[@class="product-item__name"]/text()'
    brand = '//div[@class="product-item__brand"]/p[@class]/text()'
    #regular_price = '//span[@class="product-prices__value"]/text()'  #does not append empty names
    #regular_price might not exist sometimes
    online_price = '//span[@class="product-prices__value product-prices__value--best-price"]/text()'
    #link = '//div[@class="product-item__info"]/a[ends-with(@href,"/p")]' #wrong
    

    def parse(self, response):
        item_name = response.xpath(self.item_name).getall()
        brand = response.xpath(self.brand).getall()
        #regular_price = response.xpath(self.regular_price).getall()
        online_price = response.xpath(self.online_price).getall()
        #link = response.xpath(self.link).getall()

        yield{
            'items': list(zip(brand, item_name, online_price))
            #'item_name': item_name,
            #'brand': brand,
            #'regular_price': regular_price,
            #'online_price': online_price,
            #'link': link
        }
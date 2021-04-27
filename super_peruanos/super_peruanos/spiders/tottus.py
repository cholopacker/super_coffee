import scrapy   

class TottusCoffeeSpider(scrapy.Spider):
    name = 'tottus_coffee'
    start_urls = [
        'https://www.tottus.com.pe/cafe-molido-y-grano-4010161/c/'
    ]

    custom_settings = {
        'FEED_URI': 'tottus_coffee.json',
        'FEED_FORMAT': 'json',   #Para crear archivo json directamente sin necesidad de indicar en consola
        'CONCURRENT_REQUESTS': 48,  #Establece un entero para hacer n repeticiones a la vez
        'MEMUSAGE_LIMIT_MB': 2048,   #Establece cuánta RAM se puede usar
        'MEMUSAGE_NOTIFY_MAIL': ['saul.mendoza.lizana@gmail.com'],   #Notifica cuando se llega al límite de RAM
        'ROBOTSTXT_OBEY': True,  #Para obedecer el robots.txt
        'USER_AGENT': 'JuanchoTacorta',  #Para indicar usuario al servidor
        'FEED_EXPORT_ENCODING': 'utf-8' #Para no tener caracteres raros
    }
   
    
    #item_name = '//h2[@class="jsx-1651347627 name title mini"]/text()'     #wrong
    #item_details = '//h3[@class="jsx-1651347627 extra text descriptive"]/text()'   #wrong  
    #online_price = '//span[@class="list price medium  cmrPrice"]/text()'   #wrong
        

    def parse(self, response):
        item_name = response.xpath(self.item_name).getall()
        
        #regular_price = response.xpath(self.regular_price).getall()
        online_price = response.xpath(self.online_price).getall()
        #link = response.xpath(self.link).getall()

        yield{
            'items': list(zip(item_name, online_price))
            #'item_name': item_name,
            #'brand': brand,
            #'regular_price': regular_price,
            #'online_price': online_price,
            #'link': link
        }

        #Pendiente función para pasar de página
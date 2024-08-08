import scrapy
from scrapy_splash import SplashRequest
#1.导入分布式爬虫类
from scrapy_redis.spiders import RedisSpider

#2.继承分布式爬虫类
class BailuSpider(RedisSpider):
    name = "bailu"

    # 3.注销以下两行
    #allowed_domains = ["zongheng.com"]
    #start_urls = ["https://www.zongheng.com/detail/1265647?tabsName=catalogue"]

    #4.设置redis-key
    redis_key = 'py21'

    #5.设置__init__
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain','') #获取domain，如果获取不到就设置为空字符串
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(BailuSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        yield SplashRequest(
            url='https://www.zongheng.com/detail/1265647?tabsName=catalogue',
            callback=self.parse,
            args={'wait': 0.5}
        )

    def parse(self, response,**kwargs):
        works = response.xpath('//div[@class="chapter-list--wrap"]/a/@href').extract()
        works = ["https:" + work for work in works]
        for base_url in works:
            yield scrapy.Request(base_url,callback=self.info_parse)

    def info_parse(self,response):
        title = response.xpath('//div[@class="title"]/div[@class="title_txtbox"]/text()').extract_first()
        datas = response.xpath('//div[@class="reader-box"]/div[@class="content"]/p').extract()
        datas_base = []
        for data in datas:
            data = data.replace("<p>","").replace("</p>","")
            datas_base.append(data)

        yield {
            "title":title,
            "datas":datas_base,
        }



import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lxml import etree
from jianshu.items import JianshuItem


class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com']

    # 此项目用到正则表达式，所以在创建spider的时候需要添加参数　-t crawl 用来表示创建crawl模板而非basic模板
    rules = (
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.text)
        print("开始解析一个页面...........")
        html = etree.HTML(response.text)
        item = JianshuItem()
        try:
            item['title'] = html.xpath("//h1[@class='_1RuRku']/text()")[0]
            item['name'] = html.xpath("//span[@class='_22gUMi']/text()")[0]
            item['url'] = response.url.split('?')[0]
            collection = html.xpath("//div[@class='_2Nttfz']/a/span/text()")
            if collection:
                item['collection'] = ','.join(collection)
        except:
            print("error in xpath parse")
        # print("收录",collection)
        yield item

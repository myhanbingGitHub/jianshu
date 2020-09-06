# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse


class ChromeMiddleware:

    def __init__(self):
        # 加载测试浏览器
        self.driver = webdriver.Chrome(executable_path=r"D:\chromedriver\chromedriver.exe")

    # 下面类中如果是request则服务器下载资源
    # 如果是response则跳过下载资源，直接去解析response回来的数据了
    def process_request(self, request, spider):
        # 模拟人类访问页面的行为：单击收录专题按钮
        self.driver.get(request.url)
        print("访问页面...")
        # 为了防止页面加载过慢，等待x秒
        time.sleep(5)
        # 页面已经在测试浏览器中
        try:
            while True:
                # show_more = self.driver.find_element_by_class_name('H7E3vT')
                show_more = self.driver.find_element_by_xpath("//div[@class='H7E3vT']")
                if show_more:
                    self.driver.execute_script("arguments[0].click();", show_more)  # 坑: 实际页面中，元素是叠加的，直接用showmore将无法点击。
                    print('单击了 显示更多 按钮-------------------')
                else:
                    print("找不到按钮------------------")
                time.sleep(2)
        except:
            print("没有 显示更多 按钮了！！！ ")

        source = self.driver.page_source
        # 创建一个response对象，把页面信息封装进去
        r = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding="utf-8")
        print("返回一个页面")
        return r

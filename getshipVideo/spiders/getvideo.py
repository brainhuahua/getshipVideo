import scrapy
from scrapy import cmdline

from getshipVideo.items import GetshipvideoItem


class GetvideoSpider(scrapy.Spider):
    name = "getVideo"
    allowed_domains = ["www.vcg.com", "gossv-vcg.cfp.cn"]  #注意gossv-vcg.cfp.cn，爬取的源域名
    page = 3
    url = 'https://www.vcg.com/creative-video-search/5578/?page={}'.format(str(page))
    start_urls = [url]
    test = 0

    # 一级页面
    def parse(self, response):
        lists = response.xpath('//article[@class="R3J0t _13pTf"]/div[@class="_2tMKZ"]')
        # 所有article，class为R3J0t_13pTf，的div，class="_2tMKZ"的节点
        print("lists:", lists)
        item = GetshipvideoItem()
        for i in lists:
            link = i.xpath('./a/@href').get()  # href属性所带的视频链接
            desc = i.xpath('.//div[@class="_2jWqo"]/span[1]/text()').get().replace('\n', '').replace('\r', '').replace(
                ' ', '')    #名称
            item['video'] = link
            print("test: ", self.test)
            if type(item["video"]) == str and (desc.find("船") >= 0 or desc.find("舰") >= 0 or desc.find("ship") >= 0):
                print("link: ", link)
                # 请求详情页
                yield scrapy.Request(
                    url="https://www.vcg.com" + item["video"],
                    callback=self.parse_detail,
                    meta={"item": item, "desc": desc}
                )
            self.test += 1
        if self.page < 18:
            self.page += 1
            url = 'https://www.vcg.com/creative-video-search/5578/?page={}'.format(str(self.page))
            yield scrapy.Request(url=url, callback=self.parse)

    # 二级页面
    def parse_detail(self, response):
        # item = GetshipvideoItem()
        item = response.meta["item"]
        x = response.xpath('//video/@src').get()
        print("x:", x)
        item['video'] = x
        item['desc'] = response.meta['desc']
        yield item


cmdline.execute('scrapy crawl getVideo'.split())  # 转列表

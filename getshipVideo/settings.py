# Scrapy settings for getshipVideo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "getshipVideo"

FILES_STORE = r'F:\ApplyData\Python\getshipVideo\Video'  # 视频文件
SPIDER_MODULES = ["getshipVideo.spiders"]
NEWSPIDER_MODULE = "getshipVideo.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "getshipVideo (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2 #下载延迟
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False   #  关闭cookie

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   'Accept-Language': 'en',
   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
   'cookie': '''acw_tc=2760829317366168853298716e3e2b19ec758c74ef1fe0088be7c504478ae2; uuid=c8e453e9-445b-4693-8290-2d290e0cefcb; clientIp=175.13.216.46; sajssdk_2015_cross_new_user=1; Hm_lvt_5fd2e010217c332a79f6f3c527df12e9=1736616601; fingerprint=0cf8b30ea90a644df69c430267e4967f; api_token=ST-461-879c2d4f944dd8fcbac5e1be6c0167135; abBoss3=1.0; name=18815765980; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228d532c342458a96f015a4ec6de3528610%22%2C%22first_id%22%3A%22194566e7d4c1b9e-0cab70717f313c-4c657b58-1821369-194566e7d4d2b20%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%22194566e7d4c1b9e-0cab70717f313c-4c657b58-1821369-194566e7d4d2b20%22%7D; Hm_up_5fd2e010217c332a79f6f3c527df12e9=%7B%22uuid%22%3A%7B%22value%22%3A%22c8e453e9-445b-4693-8290-2d290e0cefcb%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%228d532c342458a96f015a4ec6de3528610%22%2C%22scope%22%3A1%7D%2C%22userId%22%3A%7B%22value%22%3A%228d532c342458a96f015a4ec6de3528610%22%2C%22scope%22%3A1%7D%7D; _fp_=eyJpcCI6IjE3NS4xMy4yMTYuNDYiLCJmcCI6IjBjZjhiMzBlYTkwYTY0NGRmNjljNDMwMjY3ZTQ5NjdmIiwiaHMiOiIkMmEkMDgkZ1J0UEd6TUZrRFNQWTBYSVNnY0o3T1J6TEVtQnBSTU56RjZhTHozc2NGYWZqWVJ0RGU0NjIifQ%3D%3D; Hm_lpvt_5fd2e010217c332a79f6f3c527df12e9=1736617049; ssxmod_itna=iuitPUx+2i0dGQDHD0YhtP4Qq0IUKcDDtWwkOqODlEDWwqGzDAxn40iDtgWTbPrx+d3UC68YfiY8rEubPGGj8GLrLAC=+qDHxY=DU6xqmsD435GwD0eG+DD4DWDmnHDnxAQDjxGPyn2v5CDYPDEB5DRcPDu=AhDGc1Uh9hDeKD0=THDQI+2rxDBrhA+nrO17YDecchyEO1kGf43BKD9EYDsgR6WBIpBfdPZh3jRbB3Ax0kYq0OgPo183rCVE5hrQ03iARNiQ+qKE0K3Qbxqih5fDr5In2KCi9yfdeWxphqVA0ZDDaByvhDD=; ssxmod_itna2=iuitPUx+2i0dGQDHD0YhtP4Qq0IUKcDDtWwkOqD6EfAnx0H5ax03kiWcU2ic1yDWqQP/KAkw47D8OW=YxXrhgL8tyQ1gI8YEGGgF6yWUnHg85oUky57tw+T9X20+8doTsiKYaPG2I4GcDiQ3eD==
   '''
}  # User-Agent  cookie

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "getshipVideo.middlewares.GetshipvideoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "getshipVideo.middlewares.GetshipvideoDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "getshipVideo.pipelines.GetshipvideoPipeline": 300,
}  # 管道优先级

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
#REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
#TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

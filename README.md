# Python_Scrapy_learning
Scrapy学习

## 各部分内容
### 15-1 scrapy环境搭建测试
    scrapy startproject name
    scrapy genspider name url
    scrapy crawl spiderName
### 15-2 scrapy入门：
    Request → downloaderMiddleware → response → spiders → items → pipelines → 存储
    开启Scrapy Shell： scrapy shell + 网址url
    crawler用于直接获取项目的全局设置变量，即Settings
### 15-4 Spider的使用(url配置、抓取逻辑、解析逻辑)：
    GET请求：Request方法
    POST请求：JsonRequest或者FormRequest
### 15-5 Downloader Middleware的使用(修改User-Agent、设置代理、设置重定向、失败重试、设置Cookie等)
### 15-6 Spider Middleware的使用(处理输入给Spider的Response和Spider输出的Item及Request)
### 15-7 Item Pipeline的使用--实战：爬取ssr1

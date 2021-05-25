Scrapy tutorial
===

Project guide
---
Implement scrapy crawler on googlenews page and return news information.

Install package
---
```
pip install -r requirements.txt
```
Directory Structure
---
```
tutorial/                \# project name
+--scrapy.cfg            \# deploy configuration file
+--config.py             \# config for crawler_dev.py 
+--crawler_dev.py        \# lib for parse news website 
+--requirement.txt       \# for install package
+--tutorial/             \# project's Python module, you'll import your code from here
/   +--__init__.py
/   +--items.py          \# project items definition file
/   +--middlewares.py    \# project middlewares file
/   +--pipelines.py      \# project pipelines file
/   +--settings.py       \# project settings file
/   +--spiders/          \# a directory where you put your spiders
/   /   +--__init__.py
/   /   +--crawler.py    \# define your spider crawler
```
Note that `config.py` and `crawler_dev.py` is lib which we define. They're not scrapy modules.

And all we need to do is defining what spider do.

Run spider
---
cd to `tutorial` and run:
```
scrapy crawl GoogleNews
```

If need to output json file run:
```
scrapy crawl GoogleNews -o google.json
```

Tutorial
---
Class `GoogleNewsCrawler` is where we define [spider](https://doc.scrapy.org/en/latest/topics/spiders.html) crawler do.

`GoogleNews` is spider name and `start_urls` is the site we want to crawl.

This `start_url` is GoogleNews business page. And `scapy` would request a response from  `start_urls` and send to callback function `parse`. You can change the url to the site you want.

Parse response body by BeautifulSoup and filte the title and url of all news. Scrapy also provide [selector](https://doc.scrapy.org/en/latest/topics/selectors.html) method to parse respond or you could import `lxml` or other lib you want.

Then yield to `parse_detail` parse the url we get.This function call `parse` from `crawler_dev` to parse website by url. Then yiled to [item](https://doc.scrapy.org/en/latest/topics/items.html) module and store information we get.

You can also redefine [pipeline](https://doc.scrapy.org/en/latest/topics/item-pipeline.html) module to store information into json or database.

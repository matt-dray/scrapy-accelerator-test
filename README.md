# scrapy-accelerator-test

A small work-in-progress investigation into using Scrapy to extract elements from web pages, [following the tutorial from the Scrapy docs](https://docs.scrapy.org/en/latest/intro/tutorial.html).

The current function is to visit a couple of pages and extract some HTML elements (title and h1 tags) and write them to CSV.

The crawler can be executed by running the following at the command line:

```{sh}
scrapy crawl titles -o rostrum-titles.csv
```

Where 'titles' is the name of the spider (the code for which is in `rostrumScrape/spiders/rostrum_spider.py`) and 'rostrum-titles.csv' is the file being written to.

The example uses [my own blog site](https://rostrum.blog/). (I sanction myself to scrape my own site.)

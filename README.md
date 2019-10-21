# scrapy-accelerator-test

## What

A titchy work-in-progress investigation into using [Scrapy](https://scrapy.org/) to extract elements from web pages, [following the tutorial from the Scrapy docs](https://docs.scrapy.org/en/latest/intro/tutorial.html).

A spider in this repo is designed to visit a couple of web pages from [my own blog site](https://rostrum.blog/) (surprise, I sanctioned myself to scrape my own site), extracts some HTML elements and writes them to CSV.

## How to

From the command line, first clone this repository and then navigate to the `spider` directory (mind your fingers; this is where the spiders live). Let's say you cloned the repo to your `Documents/` directory on macOS:

```{sh}
cd ~/Documents
git clone https://github.com/matt-dray/scrapy-accelerator-test.git
cd scrapy-accelerator-test/rostrumScrape/rostrumScrape/spiders
pwd
```

The spider called 'titles' (because it extracts 'title' and 'H1' elements from the page) is found in the `rostrum_spider.py` file. It can be executed by running the following at the command line:

```{sh}
scrapy crawl titles -o rostrum-titles.csv
```

So `titles` is the spider name and `rostrum-titles.csv` is the file being written to.

Note that if you re-run the spider, the CSV will be _appended to_ rather than overwritten.

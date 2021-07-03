
import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class ScrapyWebScraper(scrapy.Spider):

    name = 'ScrapyWebScraper'
    start_urls = ['https://feudiliman.edu.ph/academics']
 
    def scrape(self):
        self.process = CrawlerProcess(settings = {
            'FEED_URI' : f'{self.name}.csv',
            'FEED_FORMAT' : 'csv'
        })
        self.process.crawl(ScrapyWebScraper)
        self.process.start()
            
    # Step 2: Parse
    def parse(self, response):
        colleges = response.css('div.content li::text').getall()
        for college in colleges:
            yield {
                'course' : college.strip(),
                'type' : 'College' if college.strip().startswith('B.') else 'Senior High'
            }
                        
    # Step 3: Output
    def output(self):
        return pd.read_csv(f'{self.name}.csv')
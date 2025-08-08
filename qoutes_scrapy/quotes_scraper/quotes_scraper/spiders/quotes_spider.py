import scrapy
from ..items import BooksScraperItem 

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'https://books.toscrape.com/catalogue/page-1.html',
    ]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            item = BooksScraperItem()
            item['title'] = book.css('h3 a::attr(title)').get()
            item['price'] = book.css('div.product_price p.price_color::text').get()
            item['availability'] = book.css('div.product_price p.instock.availability::text').re_first('\S+')
            item['rating'] = book.css('p.star-rating::attr(class)').re_first('star-rating\s+(\w+)')
            item['product_page_url'] = response.urljoin(book.css('h3 a::attr(href)').get())

            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)





# # quotes_scraper/spiders/quotes_spider.py

# import scrapy
# from ..items import QuoteItem

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"  # Unique name for the spider
#     start_urls = [
#         'https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
#         # 'http://quotes.toscrape.com/page/1/',
#     ]

#     def parse(self, response):
#         # This method is called to handle the response downloaded for each request made.
        
#         # We use CSS selectors to find the HTML elements containing the data.
#         all_div_quotes = response.css('div.quote')
        
#         # Create an instance of our item
#         items = QuoteItem()

#         for quote_div in all_div_quotes:
#             # Extract data using CSS selectors
#             text = quote_div.css('span.text::text').extract_first()
#             author = quote_div.css('.author::text').extract_first()
#             tags = quote_div.css('.tag::text').extract()
            
#             # Populate the item fields
#             items['text'] = text
#             items['author'] = author
#             items['tags'] = tags

#             # Yield the populated item to the Scrapy engine
#             yield items

#         # Find the 'Next' button link and follow it if it exists
#         next_page = response.css('li.next a::attr(href)').get()

#         if next_page is not None:
#             # The 'response.follow' method handles relative URLs automatically
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
#             yield response.follow(next_page, callback=self.p
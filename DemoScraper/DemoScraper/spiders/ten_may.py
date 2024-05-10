
import scrapy

class ManishSpider(scrapy.Spider):
    name = 'manish'
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static/computers/tablets']

    def parse(self, response):
        # Scrape data from current page
        self.scrape_page(response)

        # Check if there's a next page
        next_page = response.css('ul.pagination li.page-item.active + li.page-item a.page-link::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def scrape_page(self, response):
        products = response.css('div.card.thumbnail')
        for product in products:
            name = product.css('a.title::text').get()
            price = product.css('h4.price::text').get()
            review_count = product.css('p.review-count::text').get().split()[0]
            rating = len(product.css('span.ws-icon.ws-icon-star'))

            print("Product Name:", name)
            print("Product Price:", price)
            print("Review Count:", review_count)
            print("Rating:", rating, "stars")
            print()

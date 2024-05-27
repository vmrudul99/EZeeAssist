import os
import scrapy
from scrapy.cmdline import execute
from franchisesuppliernetwork.items import FranchisesuppliernetworkItem


def extract_data_with_path(xpath, response, method='getall'):
    if method == 'get':
        data = response.xpath(xpath).get(default='')
        return data.strip() if data else ''
    data = response.xpath(xpath).getall()
    return [item.strip() for item in data if item.strip()] if data else []

class FranchisesuppliernetworkSpider(scrapy.Spider):
    name = "franchisesuppliernetwork"
    allowed_domains = ["franchisesuppliernetwork.com"]
    start_urls = ["https://franchisesuppliernetwork.com/resources/"]
    output_folder = "output_files"

    def parse(self, response):
        if response.status == 200:
            read_more_links = extract_data_with_path('//div[contains(@class,"news-container")]/div//a[contains(text(),"Read More")]/@href',response)
            for read_more_link in read_more_links:
                yield scrapy.Request(read_more_link, callback=self.details, dont_filter=True)

            next_page = response.xpath('//a[contains(@rel,"next")]/@href').get()
            if next_page:
                yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)

    def details(self, response):
        if response.status == 200:

            post_id = extract_data_with_path('//article[@id]/@id', response, 'get')
            post_title = extract_data_with_path('//h1[@class="title"]/text()', response, 'get')
            post_date = extract_data_with_path('//span[contains(@class,"posted-on")]//time/text()', response, 'get')
            author_name = extract_data_with_path('//span[contains(@class,"author")]/text()', response, 'get')
            post_detail = extract_data_with_path('//article//div[@class="row"]//text()', response)
            post_image = extract_data_with_path('//article//img[@src]/@src', response,'get')

            folder_name = os.path.join(self.output_folder, f"article_{post_id}")
            os.makedirs(folder_name, exist_ok=True)

            with open(os.path.join(folder_name, f"{post_id}.txt"), 'w', encoding='utf-8') as text_file:
                text_file.write('\n'.join(post_detail))
            image_name = f"image_{post_id}.jpg"
            item = FranchisesuppliernetworkItem()
            item['resource URL'] = response.url
            item['resource id'] = post_id
            item['resource post date'] = post_date
            item['resource title'] = post_title
            item['resource author name'] = author_name
            item['text_name'] = f"{post_id}.txt"
            item['image_name'] = image_name
            item['image_url'] = post_image
            item['folder name'] = f"article_{post_id}"
            item['full folder path'] = folder_name
            yield item




if __name__ == '__main__':
    execute('scrapy crawl franchisesuppliernetwork -o data_resources_summary.csv'.split())

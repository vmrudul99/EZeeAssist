import os
import scrapy
import boto3
from scrapy.pipelines.images import ImagesPipeline

output_folder = "output_files"

class CustomImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        folder_name = item['folder name']
        full_folder_name = item['full folder path']
        image_name = item['image_name']
        post_id = item['resource id']
        image_url = item.get('image_url', '')
        request = scrapy.Request(image_url)
        request.meta['folder name'] = folder_name
        request.meta['full folder path'] = full_folder_name
        request.meta['image_name'] = image_name
        request.meta['resource id'] = post_id
        return request

    def file_path(self, request, response=None, info=None):
        folder = request.meta['folder name']
        image_name = request.meta['image_name']
        # post_id = request.meta['resource id']
        return f'{folder}//{image_name}'

class RemoveImagesPipeline:
    def process_item(self, item, spider):
        if 'images' in item:
            del item['images']
        return item

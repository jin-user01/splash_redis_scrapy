# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RedisXiaoshuoPipeline:

    def process_item(self, item, spider):
        with open(f"E:\\白鹿忘机\\{item['title']}.txt",'a',encoding='utf-8') as f:
            f.write(f"{item['title']}\n")
            for data in item['datas']:
                f.write(f"{data}\n")
                f.flush()

        return item

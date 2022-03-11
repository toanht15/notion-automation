#!/usr/local/bin/python3.9

import os
import sys
from pprint import pprint
from notion_client import Client

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
print("date and time =", dt_string)

# https://www.notion.so/6eb96588761f46718d3938425014a368?v=4e4655c391aa4de5b38c5eae8393fd13

os.environ['NOTION_TOKEN'] = 'secret_goUPYlSu9MUq2P3CZd6yXJpogfJkGLU5H9xxZQhoNo4'
notion = Client(auth=os.environ['NOTION_TOKEN'])

database_id = '6eb96588761f46718d3938425014a368'

# title = sys.argv[1]
# pprint(title)

new_page_props = {
        'Item': {'title': [{'text': {'content': dt_string}}]},
        'Quantity': {'number': 3},
        'Category': {'type': 'select', 'select': {'name': "Other"}},
        'Status': {'type': 'select', 'select': {'name': "Cần mua ngay"}},
        # 'Value': {'number': page_id},
        # 'Link': {'type': 'url', 'url': f"http://examples.org/page/{page_id}"},
        # 'Tags': {'type': 'multi_select', 'multi_select': [{'name': rand_page_type}]}
    }

notion_page = notion.pages.create(
    parent={'database_id': database_id},
    properties=new_page_props
)

# print(notion_page)

if notion_page['object'] == 'error':
        print("ERROR", notion_page['message'])

# db = notion.databases.query(
#     **{
#         'database_id' : database_id  # データベースID
#        }
# )

# pprint(db)
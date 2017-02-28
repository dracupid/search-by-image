#! /usr/local/bin/python3
import json
import sys

from search_same_image import search_same_image
from upload_image import upload_img_path

file_path: str = sys.argv[1]

if file_path is None:
    raise Exception("Need a file path argument")

url = file_path if file_path.startswith("http") else upload_img_path(file_path)

print("image url -> " + url)
results = search_same_image(url)

print("find %s result" % (len(results),))

with open("result.json", 'w', encoding='UTF-8') as fd:
    json.dump(results, fd, indent=2, ensure_ascii=False)

with open("result.txt", 'w', encoding='UTF-8') as fd:
    texts = list(map(lambda x: [x['fromPageTitle'], x['textHost']], results))
    json.dump(texts, fd, indent=2, ensure_ascii=False)

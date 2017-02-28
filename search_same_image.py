import math
from urllib.parse import quote

from request import get_json


def assemble_url(img_url: str, page_num: int, item_per_page: int = 10) -> str:
    img_url = quote(img_url, safe="")
    return "http://image.baidu.com/n/same?queryImageUrl=%s&rn=%s&word=&sort=&fr=pc&pos=websource&pn=%s" % (
        img_url, item_per_page, page_num)


def search_same_image(img_url: str, item_per_page: int = 50) -> list:
    start_url = assemble_url(img_url, 0, item_per_page=item_per_page)
    print("\nsearch start url -> " + start_url + "\n")
    first_page = get_json(start_url)

    total_num = first_page['extra']['totalNum']
    page_num = math.ceil((total_num - 1) / item_per_page)

    data: list = first_page['data']
    if total_num > item_per_page:
        for i in range(1, page_num):
            url = assemble_url(img_url, i, item_per_page=item_per_page)
            page = get_json(url)
            data.extend(page['data'])
    return data



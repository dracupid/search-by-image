import os
import time
from urllib.parse import urlencode

from request import post_json

upload_url = 'http://image.baidu.com/n/image'


def upload_img_file(file_obj):
    file_name = file_obj.name
    (_, extname) = os.path.splitext(file_name)
    extname = extname[1:]
    if extname not in ['png', 'jpg', 'gif', 'jpeg']:
        raise Exception("Invalid file type " + extname)

    localtime = time.asctime(time.localtime(time.time()))

    params = {
        "fr": "html5",
        'target': 'pcSearchImage',
        'needJson': 'true',
        'id': 'WU_FILE_0',
        'name': file_name,
        'type': 'image/' + extname,
        'lastModifiedDate': localtime,
        'size': os.fstat(file_obj.fileno()).st_size
    }
    url = upload_url + "?" + urlencode(params)
    res = post_json(url, file_obj)
    return res['data']['imageUrl']


def upload_img_path(path):
    with open(path, 'rb') as fd:
        return upload_img_file(fd)

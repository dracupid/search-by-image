import requests

_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) ' +
                  'Chrome/55.0.2883.95 Safari/537.36'
}


def get(url, headers=_headers, timeout=8):
    return requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)


def get_json(url, headers=_headers, timeout=8):
    res = get(url, headers=headers, timeout=timeout)
    return res.json()


def post(url, body, headers=_headers):
    return requests.post(url, headers=headers, data=body)


def post_json(url, body, headers=_headers):
    res = post(url, body, headers=headers)
    return res.json()

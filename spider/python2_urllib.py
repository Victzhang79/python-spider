# coding:utf8

import urllib2
import json

if __name__ == '__main__':
    url = 'https://www.huobi.pro/-/x/hb/p/api/contents/pro/list_notice?r=filwtz8nalu&page=2&limit=10&language=zh-cn'
    headers_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 '
                      'Safari/537.36 ',
        'Refefer': url
    }

    req = urllib2.Request(url=url, headers=headers_)
    res = urllib2.urlopen(req)
    this_page = res.read()

    print(this_page)
    print(json.dumps(json.loads(this_page)['data']['items'], ensure_ascii=False))


def get_response(url_address):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 '
                      'Safari/537.36 ',
        'Refefer': url_address
    }
    req = urllib2.Request(url=url_address, headers=headers)
    res = urllib2.urlopen(req)
    this_page = res.read()

    return json.dumps(json.loads(this_page)['data']['items'], ensure_ascii=False)

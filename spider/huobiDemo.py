# coding:utf8
import json

import pymysql
import requests
from flask import Flask, request

huoBi_url = 'https://www.huobipro.com/-/x/hb/p/api/contents/pro/list_notice?page={}&limit={}&language=zh-cn'
huoBi_detail_url = 'https://www.huobipro.com/-/x/hb/p/api/contents/pro/notice/{}'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 ' \
            'Safari/537.36'
headers = {'User-Agent': userAgent}

if __name__ == '__main__':
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='py_storage',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = db.cursor()

app = Flask(__name__)


@app.route('/api/huobi/<int:limit>/<int:page>', methods=['GET'])
def test(limit=1, page=1):
    response = requests.request('GET', huoBi_url.format(page, limit), headers=headers)
    print(response)
    # print(response.text)
    print(response.content.decode('utf-8'))  # 用context方法获取二进制内容再decode，防止乱码
    content = response.content.decode('utf-8')
    print(json.loads(content))
    print(response.json())
    print(type(response.json()))
    # 加上ensure_ascii=False后data返回的就是中文而不是unicode
    return json.dumps(json.loads(content)['data']['items'], ensure_ascii=False)
    # return json.dumps({'limit': limit, 'page': page})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)

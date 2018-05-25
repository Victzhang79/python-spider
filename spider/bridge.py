# coding:utf8

import datetime
import json
import pymysql
from flask import Flask, request
import urllib2


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def get_response(url_address):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.162 Safari/537.36 ',
        'Refefer': url_address
    }
    req = urllib2.Request(url=url_address, headers=headers)
    res = urllib2.urlopen(req)
    this_page = res.read()
    # return json.dumps(json.loads(this_page), ensure_ascii=False, cls=DateEncoder)
    return this_page


app = Flask(__name__)


@app.route('/api/bridge', methods=['GET'])
def notice_list():
    return get_response(request.args.get('url_address'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8081)

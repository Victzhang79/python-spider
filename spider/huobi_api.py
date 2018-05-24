import datetime
import json

import pymysql
from flask import Flask, request


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def check_positive_number(value):
    if value is None:
        return False
    if str(value).isdigit() and int(value) > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    db = pymysql.connect(
        host='101.201.140.96',
        port=3306,
        user='root',
        password='Galaxy@91',
        db='coin',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = db.cursor()

app = Flask(__name__)

select_notice_sql = 'select notice.id, market_id, market.name, market_notice_id, ' \
             'title, content, source, top_notice, weight, created ' \
             'from notice, market where notice.market_id = market.id limit %d, %d '

select_notice_detail_sql = 'select notice_id, market_id, market_notice_id, ' \
             'title, content, source, top_notice, weight, created ' \
             'from notice_detail where %s '


@app.route('/api/huobi/<int:limit>/<int:page>', methods=['GET'])
def notice_list(limit=None, page=None):
    if not check_positive_number(limit) or (not check_positive_number(page)):
        return 'params should be bigger than 0'
    exec_sql = select_notice_sql % ((page-1) * limit, limit)
    cursor.execute(exec_sql)
    data = cursor.fetchall()
    return json.dumps(data, cls=DateEncoder, ensure_ascii=False)


@app.route('/api/detail', methods=['GET'])
def notice_detail():
    notice_id = request.args.get('notice_id')
    market_notice_id = request.args.get('market_notice_id')
    p = ''
    if not check_positive_number(notice_id) and (not check_positive_number(market_notice_id)):
        return 'params should be present and bigger than 0'
    if check_positive_number(notice_id):
        p = 'notice_id = %s' % notice_id
    else:
        p = 'market_notice_id = %s' % market_notice_id
    exec_sql = select_notice_detail_sql % p
    cursor.execute(exec_sql)
    data = cursor.fetchone()
    return json.dumps(data, cls=DateEncoder, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8081)
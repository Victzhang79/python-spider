from datetime import datetime

import pymysql

insert_sql = 'insert into notice' \
                 '(market_id, market_notice_id, title, created, source, content, top_notice, weight)values' \
                 '(1, %d, "%s", "%s", "%s", "%s", "%s", %d)'

db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='coin',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

d_str = datetime.fromtimestamp(1527128063).strftime("%Y-%m-%d %H:%M:%S")

cursor = db.cursor()

exec_sql = insert_sql % (1, "title1", d_str, "source1", "content1", "top_notice_1", 1)

print(exec_sql)

cursor.execute(exec_sql)

cursor.close()

db.commit()

db.close()

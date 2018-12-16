import MySQLdb

conn = MySQLdb.connect(
    user=setting.SQL_USER,
    passwd=setting.SQL_PASSWORD,
    host=setting.SQL_HOST,
    db=setting.SQL_DB
)
c = conn.cursor()

# テーブル一覧の取得
sql = 'show tables'
c.execute(sql)
print('===== テーブル一覧 =====')
print(c.fetchone())

# 1レコードの登録 (重複するレコードは登録しない)
sql = 'insert ignore into table_name values (%s, %s, %s, %s)'
c.execute(sql, (val1, val2, val3, val4))  # 1件のみ

# レコードの取得
sql = 'select * from table_name'
c.execute(sql)
print('===== レコード =====')
for row in c.fetchall():
    print('Id:', row[0], 'Content:', row[1:])

# データベースへの変更を保存
conn.commit()

c.close()
conn.close()

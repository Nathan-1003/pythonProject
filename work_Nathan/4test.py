import json
import re
import pymysql  #pip3 install PyMySQL ,pip install mysql-connector-python
import flask
import datetime
from flask import Flask, render_template

db = pymysql.connect(host='34.142.180.39',
                     port=13306,
                     user='root',
                     passwd='oh_my_ody!',
                     db = 'data_center',
                     charset='utf8')
#def test_select_channel():

#sql_cmd = 'SELECT channel_id FROM data_center.channel GROUP BY channel_id ORDER BY channel_id'
sql_cmd = 'SELECT * FROM data_center.channel LIMIT 5 '
cur=db.cursor()
cur.execute(sql_cmd)#執行sql
# result = cur.fetchall()#取出返回的結果值_tuple
headers = [description[0] for description in cur.description]# 取得表的標題
#print(headers)
results = cur.fetchall()#查詢結果
#print(results)
data = [dict(zip(headers, row)) for row in results]#將表的標題和查詢結果組合成字典
print(data)

# for key,value in data[0].items():
#     print('{key}:{value}'.format(key=key, value=value))

cur.close()

app = flask.Flask(__name__)
@app.route("/")

def hello():
    return(data)

if __name__ == '__main__':
    app.run()




# print()
# for row in cur:
#     print(row)
# cur.close()















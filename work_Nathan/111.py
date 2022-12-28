import requests
import json
import numpy as np
import time
import datetime
import re

today = datetime.date.today()
date_begintime_stamp=int(time.mktime(today.timetuple())) - 86400
date_begintime_stamp=date_begintime_stamp*1000
date_endtime_stamp=(date_begintime_stamp+86399*1000+999)
print(date_begintime_stamp)
print(date_endtime_stamp)

url = 'http://8.219.83.66:8088/admin/v2/login'
headers = {"Content-Type": "application/json"}
data = '{"username":"admin","password":"1234"}'
# data = {'username':'admin','password':'1234'}
# data=json.dumps(data)
r = requests.post(url, headers=headers, data=data)
#print(r.text) #成功登入資訊
t = json.loads(r.text)#抓取token
token = t["token"] #抓取token欄位數值

#print(token)

def channels():#總表
    url = ' http://8.219.83.66:8088/admin/v2/system/dict/data/channels'
    headers = {"Content-Type": "application/json","Authorization": token }
    data = {'pageNum':'1','pagesize':'10000'} #這種寫法可以放東西引用
    data = '{"pageNum":"1","pagesize":"10000"}'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)
#首頁
def rechargeCashoutDiff():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/rechargeCashoutDiff/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    #data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    data = {'beginTime': date_begintime_stamp,#1668960000000
            'channelId': '',
            'currency': '',
            'device':'',
            'endTime': date_endtime_stamp,#1669046399999
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    #print(_data)
    #print(r)
    response = r.json()  # 轉json
    #print(response)
    #print(response["data"]["rechargeCashoutDiff"])

    print(list(response["data"].values()))
    if (list(response["data"].values())) == 0:
        print("x")



    # for key,value in response["data"]:

    # if response["data"]["rechargeCashoutDiff"] == 0:
    #     print("rechargeCashoutDiff_Error")
    # if response["data"]["activityDetailCount"] == 0:
    #     print("activityDetailCount_Error")
    # if response["data"]["activityMoney"] == 0:
    #     print("activityMoney_Error")
    # if response["data"]["activityUserCount"] == 0:
    #     print("activityUserCount_Error")
    # if response["data"]["cashout"] == 0:
    #     print("cashout_Error")
    # if response["data"]["cashoutCount"] == 0:
    #     print("cashoutCount_Error")
    # if response["data"]["cashoutUsers"] == 0:
    #     print("cashoutUsers_Error")
    # if response["data"]["manualRechargeGift"] == 0:
    #     print("manualRechargeGift_Error")
    # if response["data"]["manualRechargeGiftCount"] == 0:
    #     print("manualRechargeGiftCount_Error")
    # if response["data"]["onlineRecharge"] == 0:
    #     print("onlineRecharge_Error")
    # if response["data"]["onlineRechargeCount"] == 0:
    #     print("onlineRechargeCount_Error")
    # if response["data"]["onlineRechargeUsers"] == 0:
    #     print("onlineRechargeUsers_Error")
    # if response["data"]["rechargeCashoutDiff"] == 0:
    #     print("rechargeCashoutDiff_Error")
    # else :
    #     print("數據總表充提差(13)_Check OK")

if __name__== '__main__':
    rechargeCashoutDiff()#數據總表
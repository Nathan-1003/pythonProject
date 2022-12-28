import requests
import json
import numpy as np
import time
import datetime;

today = datetime.date.today()
date_begintime_stamp=int(time.mktime(today.timetuple())) - 86400
date_begintime_stamp=date_begintime_stamp*1000
date_endtime_stamp=(date_begintime_stamp+86399*1000+999)
#print(date_begintime_stamp)#1668960000000
#print(date_endtime_stamp)#1669046399999

url = 'http://8.219.83.66:8088/admin/v2/login'
headers = {
    "Content-Type": "application/json"
}
data = '{"username":"admin","password":"1234"}'
r = requests.post(url, headers=headers, data=data)
#print(r.text) #成功登入
t = json.loads(r.text)#定義token取用
token = t["token"] #response提取的token使用
#print(token)

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
    #print(type(response["data"]))
    # print(response["data"])
    for key,value in response["data"].items():
        if key !="rechargeCashoutChartValue":
            print('{key}:{value}'.format(key = key , value = value))
    # for key in response["data"].keys():
    #     print('key = {}'.format(key))
    # for value in response["data"].values():
    #     print('value = {}'.format(value))


    if response["data"]["rechargeCashoutDiff"] == 0:
        print("rechargeCashoutDiff_Error")
    if response["data"]["activityDetailCount"] == 0:
        print("activityDetailCount_Error")
    if response["data"]["activityMoney"] == 0:
        print("activityMoney_Error")
    if response["data"]["activityUserCount"] == 0:
        print("activityUserCount_Error")
    if response["data"]["cashout"] == 0:
        print("cashout_Error")
    if response["data"]["cashoutCount"] == 0:
        print("cashoutCount_Error")
    if response["data"]["cashoutUsers"] == 0:
        print("cashoutUsers_Error")
    if response["data"]["manualRechargeGift"] == 0:
        print("manualRechargeGift_Error")
    if response["data"]["manualRechargeGiftCount"] == 0:
        print("manualRechargeGiftCount_Error")
    if response["data"]["onlineRecharge"] == 0:
        print("onlineRecharge_Error")
    if response["data"]["onlineRechargeCount"] == 0:
        print("onlineRechargeCount_Error")
    if response["data"]["onlineRechargeUsers"] == 0:
        print("onlineRechargeUsers_Error")
    else:
        print("OK")

def newRegCount():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/newRegCount/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime':date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'device':'',
            'endTime':date_endtime_stamp,
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    #print(_data)
    # print(r)
    response = r.json()  # 轉json
    # print(response)
    for key,value in response["data"].items():
        if key !=("onlineUser","dailyAvgAct"):# !=>>key=該名及排除
            print('{key}:{value}'.format(key = key , value = value))
    # if response["data"]["activeOnline"] == 0:
    #     print("activeOnline_Error")
    if response["data"]["dailyAvgAct"] == 0:
        print("dailyAvgAct_Error")
    if response["data"]["dailyAvgOnline"] == 0:
        print("dailyAvgOnline_Error")
    if response["data"]["newRegCount"] == 0:
        print("newRegCount_Error")
    if response["data"]["onlinePodcast"] == 0:
        print("onlinePodcast_Error")
    # if response["data"]["onlineUser"] == 0:
    #     print("onlineUser_Error")
    if response["data"]["totalBindCount"] == 0:
        print("totalBindCount_Error")
    if response["data"]["totalRegCount"] == 0:
        print("totalRegCount_Error")
    else :
        print("數據總表新增會員欄位(6)_Check OK")

if __name__== '__main__':
    rechargeCashoutDiff()
    # newRegCount()

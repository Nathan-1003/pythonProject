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
token = t["token"] #response提取的token使用

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
    # print(r)
    response = r.json()  # 轉json
    # print(response)
    #print(response["data"]["rechargeCashoutDiff"])
    print('--------首頁_充提差(13)--------')
    for key,value in response["data"].items():
        if key !=("rechargeCashoutChartValue"):# !=>>key=該名及排除
            print('{key}:{value}'.format(key = key , value = value))
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
    if response["data"]["rechargeCashoutDiff"] == 0:
        print("rechargeCashoutDiff_Error")
    else :
        print("數據總表充提差(13)_Check OK")
#首頁
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
    print('--------首頁_新增會員數(6)--------')
    for key,value in response["data"].items():
        if key != "onlineUser" and key !="activeOnline" :# !=>>key=該名及排除
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
#首頁
def firstDayPayRate():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/firstDayPayRate/'
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
    print('--------首頁_付費率(5)--------')
    for key,value in response["data"].items():
        if key != "secondRecharge" and key !="secondRechargeMoney" :# !=>>key=該名及排除
            print('{key}:{value}'.format(key = key , value = value))
    if response["data"]["firstDayPayRate"] == 0:
        print("firstDayPayRate_Error")
    if response["data"]["firstRecharge"] == 0:
        print("firstRecharge_Error")
    if response["data"]["firstRechargeMoney"] == 0:
        print("firstRechargeMoney_Error")
    if response["data"]["firstRechargeRate"] == 0:
        print("firstRechargeRate_Error")
    # if response["data"]["secondRecharge"] == 0:
    #     print("secondRecharge_Error")
    # if response["data"]["secondRechargeMoney"] == 0:
    #     print("secondRechargeMoney_Error")
    if response["data"]["secondRechargeRate"] == 0:
        print("secondRechargeRate_Error")
    else :
        print("數據總表付費率(5)_Check OK")
#首頁
def agentData():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/agentData/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'device':'',
            'endTime': date_endtime_stamp,
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    #print(_data)
    # print(r)
    response = r.json()
    print('--------首頁_代理數據(3)--------')
    for key,value in response["data"].items():
        if key != "agentAvailableBetNum" and key !="agentGameBonus" and key !="agentLiveBonus"and key !="agentSubChannelCount"and key !="agentTotalBonus"and key !="agentUserCount":# !=>>key=該名及排除
            print('{key}:{value}'.format(key = key , value = value))
    # print(response)
    # if response["data"]["agentAvailableBetNum"] == 0:
    #     print("agentAvailableBetNum_Error")
    # if response["data"]["agentGameBonus"] == 0:
    #     print("agentGameBonus_Error")
    # if response["data"]["agentLiveBonus"] == 0:
    #     print("agentLiveBonus_Error")
    if response["data"]["totalAgentGameBonus"] == 0:
        print("totalAgentGameBonus_Error")
    if response["data"]["totalAgentLiveBonus"] == 0:
        print("totalAgentLiveBonus_Error")
    if response["data"]["totalAgentTotalBonus"] == 0:
        print("totalAgentTotalBonus_Error")
    else :
        print("數據總表代理數據(3)_Check OK")
#首頁
def gameData():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/gameData/'
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
    # print(_data)
    # print(r)
    response = r.json()
    print('--------首頁_遊戲數據(52)--------')
    for key,value in response["data"].items():
        if key !="djCount" and key !="djIncome" and key !="djAvailableBetSum" and key !="djKillRate" and key !="djTotalBet" and key !="djUserCount":
            print('{key}:{value}'.format(key = key , value = value))
    if response["data"]["boinLotteryAvailableBetSum"] == 0:
        print("boinLotteryAvailableBetSum_Error")
    if response["data"]["boinLotteryCount"] == 0:
        print("boinLotteryCount_Error")
    if response["data"]["boinLotteryIncome"] == 0:
        print("boinLotteryIncome_Error")
    if response["data"]["boinLotteryKillRate"] == 0:
        print("boinLotteryKillRate_Error")
    if response["data"]["boinLotteryTotalBet"] == 0:
        print("boinLotteryTotalBet_Error")
    if response["data"]["boinLotteryUserCount"] == 0:
        print("boinLotteryUserCount_Error")
    if response["data"]["cardsChessAvailableBetSum"] == 0:
        print("cardsChessAvailableBetSum_Error")
    if response["data"]["cardsChessCount"] == 0:
        print("cardsChessCount_Error")
    if response["data"]["cardsChessIncome"] == 0:
        print("cardsChessIncome_Error")
    if response["data"]["cardsChessKillRate"] == 0:
        print("cardsChessKillRate_Error")
    if response["data"]["cardsChessTotalBet"] == 0:
        print("cardsChessTotalBet_Error")
    if response["data"]["cardsChessUserCount"] == 0:
        print("cardsChessUserCount_Error")
    # if response["data"]["djAvailableBetSum"] == 0:
    #     print("djAvailableBetSum_Error")
    # if response["data"]["djCount"] == 0:
    #     print("djCount_Error")
    # if response["data"]["djIncome"] == 0:
    #     print("djIncome_Error")
    # if response["data"]["djKillRate"] == 0:
    #     print("djKillRate_Error")
    # if response["data"]["djTotalBet"] == 0:
    #     print("djTotalBet_Error")
    # if response["data"]["djUserCount"] == 0:
    #     print("djUserCount_Error")
    if response["data"]["egameAvailableBetSum"] == 0:
        print("egameAvailableBetSum_Error")
    if response["data"]["egameCount"] == 0:
        print("egameCount_Error")
    if response["data"]["egameIncome"] == 0:
        print("egameIncome_Error")
    if response["data"]["egameKillRate"] == 0:
        print("egameKillRate_Error")
    if response["data"]["egameTotalBet"] == 0:
        print("egameTotalBet_Error")
    if response["data"]["egameUserCount"] == 0:
        print("egameUserCount_Error")
    if response["data"]["fishingAvailableBetSum"] == 0:
        print("fishingAvailableBetSum_Error")
    if response["data"]["egameCount"] == 0:
        print("egameCount_Error")
    if response["data"]["egameIncome"] == 0:
        print("egameIncome_Error")
    if response["data"]["egameKillRate"] == 0:
        print("egameKillRate_Error")
    if response["data"]["egameTotalBet"] == 0:
        print("egameTotalBet_Error")
    if response["data"]["egameUserCount"] == 0:
        print("egameUserCount_Error")
    if response["data"]["fishingAvailableBetSum"] == 0:
        print("fishingAvailableBetSum_Error")
    if response["data"]["fishingCount"] == 0:
        print("fishingCount_Error")
    if response["data"]["fishingIncome"] == 0:
        print("fishingIncome_Error")
    if response["data"]["fishingKillRate"] == 0:
        print("fishingKillRate_Error")
    if response["data"]["fishingTotalBet"] == 0:
        print("fishingTotalBet_Error")
    if response["data"]["fishingUserCount"] == 0:
        print("fishingUserCount_Error")
    if response["data"]["lotteryAvailableBetSum"] == 0:
        print("lotteryAvailableBetSum_Error")
    if response["data"]["lotteryCount"] == 0:
        print("lotteryCount_Error")
    if response["data"]["lotteryIncome"] == 0:
        print("lotteryIncome_Error")
    if response["data"]["lotteryKillRate"] == 0:
        print("lotteryKillRate_Error")
    if response["data"]["lotteryTotalBet"] == 0:
        print("lotteryTotalBet_Error")
    if response["data"]["lotteryUserCount"] == 0:
        print("lotteryUserCount_Error")
    if response["data"]["realAvailableBetSum"] == 0:
        print("realAvailableBetSum_Error")
    if response["data"]["realCount"] == 0:
        print("realCount_Error")
    if response["data"]["realIncome"] == 0:
        print("realIncome_Error")
    if response["data"]["realKillRate"] == 0:
        print("realKillRate_Error")
    if response["data"]["realTotalBet"] == 0:
        print("realTotalBet_Error")
    if response["data"]["realUserCount"] == 0:
        print("realUserCount_Error")
    if response["data"]["sportAvailableBetSum"] == 0:
        print("sportAvailableBetSum_Error")
    if response["data"]["sportCount"] == 0:
        print("sportCount_Error")
    if response["data"]["sportIncome"] == 0:
        print("sportIncome_Error")
    if response["data"]["sportKillRate"] == 0:
        print("sportKillRate_Error")
    if response["data"]["sportTotalBet"] == 0:
        print("sportTotalBet_Error")
    if response["data"]["sportUserCount"] == 0:
        print("sportUserCount_Error")
    if response["data"]["totalAvailableBetSum"] == 0:
        print("totalAvailableBetSum_Error")
    if response["data"]["totalBet"] == 0:
        print("totalBet_Error")
    if response["data"]["totalBetUserCount"] == 0:
        print("totalBetUserCount_Error")
    if response["data"]["totalIncome"] == 0:
        print("totalIncome_Error")
    # if response["data"]["unknownAvailableBetSum"] == 0:
    #     print("unknownAvailableBetSum_Error")
    # if response["data"]["unknownCount"] == 0:
    #     print("unknownCount_Error")
    # if response["data"]["unknownIncome"] == 0:
    #     print("unknownIncome_Error")
    # if response["data"]["unknownKillRate"] == 0:
    #     print("unknownKillRate_Error")
    # if response["data"]["unknownTotalBet"] == 0:
    #     print("unknownTotalBet_Error")
    # if response["data"]["unknownUserCount"] == 0:
    #     print("unknownUserCount_Error")
    else :
        print("數據總表遊戲數據(52)_Check OK")
#首頁
def podcastDiamond():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/podcastDiamond/'
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
    #print(r.text)
    response = r.json()
    # print(response)
    print('--------首頁_直播數據(9)--------')
    for key,value in response["data"].items():
        if key !="podcastTotalTicket" and key !="ticketChartValue" and key !="useDiamond":
            print('{key}:{value}'.format(key = key , value = value))
    if response["data"]["compareRechargeDiamond"] == 0:
        print("compareRechargeDiamond_Error")
    if response["data"]["firstRechargeCount"] == 0:
        print("firstRechargeCount_Error")
    if response["data"]["firstRechargeDiamond"] == 0:
        print("firstRechargeDiamond_Error")
    if response["data"]["firstRechargeValue"] == 0:
        print("firstRechargeValue_Error")
    if response["data"]["podcastTotalBet"] == 0:
        print("podcastTotalBet_Error")
    if response["data"]["rechargeDiamond"] == 0:
        print("rechargeDiamond_Error")
    if response["data"]["rechargeUserCount"] == 0:
        print("rechargeUserCount_Error")
    if response["data"]["rechargeValue"] == 0:
        print("rechargeValue_Error")
    if response["data"]["ticketForPodcast"] == 0:
        print("tticketForPodcast_Error")
    # if response["data"]["useDiamond"] == 0:
    #     print("useDiamond_Error")
    else :
        print("數據總表直播數據(9)_Check OK")
#首頁
def diamondConsumption():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/diamondConsumption/'
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
    #print(r.text)
    response = r.json()
    # print(response)
    print('--------首頁_鑽石消耗(2)--------')
    if response["data"]["totalDiamond"] == 0:
        print("totalDiamond_Error")
    if response["data"]["totalUserCount"] == 0:
        print("totalUserCount_Error")
    else :
        print("數據總表鑽石消耗(2)_Check OK")

def profiles():
    url = ' http://8.219.83.66:8088/admin/dataCenter/users/profiles/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId': '',
            'currency': '',
            'device': '',
            'endTime': date_endtime_stamp,
            'groupBy':'1',
            'openChannelId': ''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    # print(_data)
    # print(r)
    response = r.json()  # 轉json
    print('--------二級頁面_會員財務數據-會員(3)--------')
    for key,value in response["data"].items():
        if key !="activities" and key !="cashes" and key !="payments":
            print('{key}:{value}'.format(key = key , value = value))
    # print(response)
    # if response["data"]["activities"] == 0:
    #     print("activities_Error")
    # if response["data"]["cashes"] == 0:
    #     print("cashes_Error")
    # if response["data"]["payments"] == 0:
    #     print("payments_Error")
    if response["data"]["totalActivity"] == 0:
        print("totalActivity_Error")
    if response["data"]["totalCash"] == 0:
        print("totalCash_Error")
    if response["data"]["totalPayment"] == 0:
        print("totalPayment_Error")
    else :
        print("數據總表_會員財務數據-會員(3)_Check OK")

def online():
    url = ' http://8.219.83.66:8088/admin/dataCenter/users/online/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId': '',
            'currency': '',
            'device': '',
            'endTime': date_endtime_stamp,
            'groupBy':'1',
            'openChannelId': ''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    # print(_data)
    # print(r)
    response = r.json()  # 轉json
    print('--------二級頁面_會員財務數據-活躍(3)--------')
    for key,value in response["data"].items():
        if key !="active"and key !="online" and key !="register" and key !="totalActive" and key !="totalOnline":
            print('{key}:{value}'.format(key = key , value = value))
    # print(response)
    # if response["data"]["active"] == 0:
    #     print("active_Error")
    if response["data"]["dailyAvgActive"] == 0:
        print("dailyAvgActive_Error")
    if response["data"]["dailyAvgOnline"] == 0:
        print("dailyAvgOnline_Error")
    # if response["data"]["online"] == 0:
    #     print("online_Error")
    # if response["data"]["register"] == 0:
    #     print("register_Error")
    #if response["data"]["totalActive"] == 0:
    #    print("totalActive_Error")
    #if response["data"]["totalOnline"] == 0:
    #    print("totalOnline_Error")
    if response["data"]["totalRegister"] == 0:
        print("totalRegister_Error")
    else :
        print("數據總表_會員財務數據-活躍(3)_Check OK")

def recharge():
    url = ' http://8.219.83.66:8088/admin/dataCenter/users/recharge/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId': '',
            'currency': '',
            'device': '',
            'endTime': date_endtime_stamp,
            'groupBy':'1',
            'openChannelId': ''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    # print(_data)
    # print(r)
    response = r.json()  # 轉json
    print('--------二級頁面_會員財務數據-首充/二充(20)--------')
    for key,value in response["data"]["dayRange"][1].items():
        if key !="avgFirstRecharge" and key !="avgSecondRecharge" and key !="firstRecharge" and key !="secondRecharge":
            print('{key}:{value}'.format(key=key, value=value))
    for key,value in response["data"]["dayRange"][2].items():
        if key != "avgFirstRecharge" and key != "avgSecondRecharge" and key != "firstRecharge" and key != "secondRecharge":
            print('{key}:{value}'.format(key=key, value=value))
    for key,value in response["data"]["dayRange"][3].items():
        if key != "avgFirstRecharge" and key != "avgSecondRecharge" and key != "firstRecharge" and key != "secondRecharge":
            print('{key}:{value}'.format(key=key, value=value))
    for key,value in response["data"]["dayRange"][4].items():
        if key != "avgFirstRecharge" and key != "avgSecondRecharge" and key != "firstRecharge" and key != "secondRecharge":
            print('{key}:{value}'.format(key=key, value=value))
    for key,value in response["data"]["dayRange"][5].items():
        if key != "avgFirstRecharge" and key != "avgSecondRecharge" and key != "firstRecharge" and key != "secondRecharge":
            print('{key}:{value}'.format(key = key , value = value))
    # print(response)
    #print(response['data']['dayRange'][1]['firstRechargeRate'])
    if response["data"]['dayRange'][1]['firstRechargeRate'] == 0:
        print("3day_firstRechargeRate_Error")
    if response["data"]['dayRange'][1]['firstRechargeCount'] == 0:
        print("3day_firstRechargeCount_Error")
    if response["data"]['dayRange'][1]['secondRechargeRate'] == 0:
        print("3day_secondRechargeRate_Error")
    if response["data"]['dayRange'][1]['secondRechargeCount'] == 0:
        print("3day_secondRechargeCount_Error")
    if response["data"]['dayRange'][2]['firstRechargeRate'] == 0:
        print("5day_firstRechargeRate_Error")
    if response["data"]['dayRange'][2]['firstRechargeCount'] == 0:
        print("5day_firstRechargeCount_Error")
    if response["data"]['dayRange'][2]['secondRechargeRate'] == 0:
        print("5day_secondRechargeRate_Error")
    if response["data"]['dayRange'][2]['secondRechargeCount'] == 0:
        print("5day_secondRechargeCount_Error")
    if response["data"]['dayRange'][3]['firstRechargeRate'] == 0:
        print("7day_firstRechargeRate_Error")
    if response["data"]['dayRange'][3]['firstRechargeCount'] == 0:
        print("7day_firstRechargeCount_Error")
    if response["data"]['dayRange'][3]['secondRechargeRate'] == 0:
        print("7day_firstRechargeRate_Error")
    if response["data"]['dayRange'][3]['secondRechargeCount'] == 0:
        print("7day_secondRechargeCount_Error")
    if response["data"]['dayRange'][4]['firstRechargeRate'] == 0:
        print("14day_firstRechargeRate_Error")
    if response["data"]['dayRange'][4]['firstRechargeCount'] == 0:
        print("14day_firstRechargeCount_Error")
    if response["data"]['dayRange'][4]['secondRechargeRate'] == 0:
        print("14day_secondRechargeRate_Error")
    if response["data"]['dayRange'][4]['secondRechargeCount'] == 0:
        print("14day_secondRechargeCount_Error")
    if response["data"]['dayRange'][5]['firstRechargeRate'] == 0:
        print("30day_firstRechargeRate_Error")
    if response["data"]['dayRange'][5]['firstRechargeCount'] == 0:
        print("30day_firstRechargeCount_Error")
    if response["data"]['dayRange'][5]['secondRechargeRate'] == 0:
        print("30day_secondRechargeRate_Error")
    if response["data"]['dayRange'][5]['secondRechargeCount'] == 0:
        print("30day_secondRechargeCount_Error")
    else:
        print("數據總表_會員財務數據-首充/二充(20)_Check OK")

def bet_blocks():
    url = ' http://8.219.83.66:8088/admin/dataCenter/bets/blocks'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId': '',
            'currency': '',
            'device': '',
            'endTime': date_endtime_stamp,
            'groupBy':'1',
            'openChannelId': ''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    # print(_data)
    # print(r)
    response = r.json()  # 轉json
    # print(response)
    print('--------二級頁面_遊戲數據(4)--------')
    for key,value in response["data"].items():
        # if key !="":
            print('{key}:{value}'.format(key = key , value = value))
    if response["data"]["availableBetTotal"] == 0:
        print("availableBetTotal_Error")
    if response["data"]["betTotal"] == 0:
        print("betTotal_Error")
    if response["data"]["gameProfit"] == 0:
        print("gameProfit_Error")
    if response["data"]["totalPeopleOfBets"] == 0:
        print("totalPeopleOfBets_Error")
    else:
        print('數據總表_遊戲數據(4)_Check OK')

def live_blocks():
    url = ' http://8.219.83.66:8088/admin/dataCenter/stream/blocks'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId': '',
            'currency': '',
            'device': '',
            'endTime': date_endtime_stamp,
            'groupBy':'1',
            'openChannelId': ''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    # print(_data)
    # print(r)
    response = r.json()  # 轉json
    print('--------二級頁面_直播數據(15)+鑽石支出(8)--------')
    # print(response['data']['pieChart']['routineConsumption'])
    for key,value in response["data"].items():
        if key !="jbcpBar" and key !="pieChart":
            print('{key}:{value}'.format(key = key , value = value))
    if response["data"]["availableBetTotal"] == 0:
        print("availableBetTotal_Error")
    if response["data"]["avgAmount"] == 0:
        print("avgAmount_Error")
    if response["data"]["avgReduce"] == 0:
        print("avgReduce_Error")
    if response["data"]["betTotal"] == 0:
        print("betTotal_Error")
    if response["data"]["diamondExchangeTotal"] == 0:
        print("diamondExchangeTotal_Error")
    if response["data"]["diamondExchangeTotalAmount"] == 0:
        print("diamondExchangeTotalAmount_Error")
    if response["data"]["exchangeTotal"] == 0:
        print("exchangeTotal_Error")
    if response["data"]["firstDiamondExchangeTotal"] == 0:
        print("firstDiamondExchangeTotal_Error")
    if response["data"]["firstExchangeTotal"] == 0:
        print("firstExchangeTotal_Error")
    if response["data"]["firstExchangeTotalAmount"] == 0:
        print("firstExchangeTotalAmount_Error")
    if response["data"]["jbcpBarBetTotal"] == 0:
        print("jbcpBarBetTotal_Error")
    if response["data"]["jbcpBarTicketTotal"] == 0:
        print("jbcpBarTicketTotal_Error")
    if response["data"]["profit"] == 0:
        print("profit_Error")
    if response["data"]["siteDiamondReducet"] == 0:
        print("siteDiamondReducet_Error")
    if response["data"]["totalProfit"] == 0:
        print("totalProfit_Error")
    for key,value in response["data"]["pieChart"].items():
        if key !="defend" and key !="guardianceEnable" and key !="proceedGuardiance" and key !="reward" and key !="transport" and key !="vip":
            print('{key}:{value}'.format(key = key , value = value))
    if response['data']['pieChart']['barrage'] == 0:
        print("barrage_Error")
    if response['data']['pieChart']['buyVip'] == 0:
        print("buyVip_Error")
    if response['data']['pieChart']['byLiveConsumption'] == 0:
        print("byLiveConsumption_Error")
    if response['data']['pieChart']['giftGiving'] == 0:
        print("giftGiving_Error")
    if response['data']['pieChart']['itemBuy'] == 0:
        print("itemBuy_Error")
    if response['data']['pieChart']['proceedVip'] == 0:
        print("proceedVip_Error")
    if response['data']['pieChart']['routineConsumption'] == 0:
        print("routineConsumption_Error")
    if response['data']['pieChart']['totalUsedDiamond'] == 0:
        print("totalUsedDiamond_Error")
    else:
        print('數據總表_直播數據(15)+鑽石支出(8)_Check OK')

def businessReport():
    url = ' http://8.219.83.66:8088/admin/dataCenter/businessReport/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId': '',
            'endTime': date_endtime_stamp,
            'isAsc':'ASC',
            'openChannelId':'',
            'orderByColumn':'channel_id',
            'pageNum':'1',
            'pageSize':'500'}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    # print(_data)
    # print(r)
    response = r.json()  # 轉json
    # print(response)
    print('--------經營報表(15)+商戶yy(15)--------')
    for key,value in response["totalData"].items():
        if key !="totalBindCount":
            print('{key}:{value}'.format(key = key , value = value))
    if response["totalData"]["availableBetSum"] == 0:
        print("availableBetSum_Error")
    if response["totalData"]["betSum"] == 0:
        print("betSum_Error")
    if response["totalData"]["cash"] == 0:
        print("cash_Error")
    if response["totalData"]["cashRechargeRate"] == 0:
        print("cashRechargeRate_Error")
    if response["totalData"]["exchangeDiamond"] == 0:
        print("exchangeDiamond_Error")
    if response["totalData"]["firstRecharge"] == 0:
        print("firstRecharge_Error")
    if response["totalData"]["firstRechargeCount"] == 0:
        print("firstRechargeCount_Error")
    if response["totalData"]["fsMoney"] == 0:
        print("fsMoney_Error")
    if response["totalData"]["playerCount"] == 0:
        print("playerCount_Error")
    if response["totalData"]["recharge"] == 0:
        print("recharge_Error")
    if response["totalData"]["rechargeCashDiff"] == 0:
        print("rechargeCashDiff_Error")
    if response["totalData"]["regCount"] == 0:
        print("regCount_Error")
    # if response["totalData"]["totalBindCount"] == 0:
    #     print("totalBindCount_Error")
    if response["totalData"]["totalUserCount"] == 0:
        print("totalUserCount_Error")
    if response["totalData"]["winBetDiff"] == 0:
        print("winBetDiff_Error")
    if response["totalData"]["winBetDiffRechargeRate"] == 0:
        print("winBetDiffRechargeRate_Error")
    for key,value in response["data"][186].items():
        if key !="totalBindCount" and key !="createAt" and key !="updateAt":
            print('{key}:{value}'.format(key = key , value = value))
    if response["data"][186]["availableBetSum"] == 0:
        print("availableBetSum_Error")
    if response["data"][186]["betSum"] == 0:
        print("betSum_Error")
    if response["data"][186]["cash"] == 0:
        print("cash_Error")
    if response["data"][186]["cashRechargeRate"] == 0:
        print("cashRechargeRate_Error")
    if response["data"][186]["exchangeDiamond"] == 0:
        print("exchangeDiamond_Error")
    if response["data"][186]["firstRecharge"] == 0:
        print("firstRecharge_Error")
    if response["data"][186]["firstRechargeCount"] == 0:
        print("firstRechargeCount_Error")
    if response["data"][186]["fsMoney"] == 0:
        print("\033[31mfsMoney_Error，This Channel NO fsMoney")
    if response["data"][186]["playerCount"] == 0:
        print("playerCount_Error")
    if response["data"][186]["recharge"] == 0:
        print("recharge_Error")
    if response["data"][186]["rechargeCashDiff"] == 0:
        print("rechargeCashDiff_Error")
    if response["data"][186]["regCount"] == 0:
        print("regCount_Error")
        # if response["totalData"]["totalBindCount"] == 0:
        #     print("totalBindCount_Error")
    if response["data"][186]["totalUserCount"] == 0:
        print("totalUserCount_Error")
    if response["data"][186]["winBetDiff"] == 0:
        print("winBetDiff_Error")
    if response["data"][186]["winBetDiffRechargeRate"] == 0:
        print("winBetDiffRechargeRate_Error")
    else :
        print("經營報表(15)+商戶yy(15)_Check OK")

def dailyReport():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dailyReport/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId': '',
            'currency':'',
            'device':'',
            'endTime': date_endtime_stamp,
            'openChannelId':'',}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    # print(_data)
    #print(r)
    response = r.json()  # 轉json
    # print(response)
    # print(list(response["data"].values()))
    # if (list(response["data"].values())) == 0:
    #print(response['data']['gameList'][0]['availableBetSum'])
    print('--------日報表-遊戲數據(6)+日報表-直播數據(8)--------')
    for key,value in response['data']['gameList'][0].items():
        if key !="availableBetSumGrowthRate" and key !="betGrowthRate" and key !="betUserCountGrowthRate" and key !="detail" and key !="fsMoneyGrowthRate" and key !="incomeGrowthRate":
            print('{key}:{value}'.format(key = key , value = value))
    if (response['data']['gameList'][0]['availableBetSum']) == 0:
        print("gameList-availableBetSum_Error")
    if (response['data']['gameList'][0]['bet']) == 0:
        print("gameList-bet_Error")
    if (response['data']['gameList'][0]['betUserCount']) == 0:
        print("gameList-betUserCount_Error")
    if (response['data']['gameList'][0]['dataTime']) == 0:
        print("gameList-dataTime_Error")
    if (response['data']['gameList'][0]['fsMoney']) == 0:
        print("gameList-fsMoney_Error")
    if (response['data']['gameList'][0]['income']) == 0:
        print("gameList-income_Error")
    else:
        print("日報表-遊戲數據(6)_Check OK")
    for key,value in response['data']['liveList'][0].items():
        if key !="activityMoneyGrowthRate" and key !="cashoutGrowthRate" and key !="diamondRechargeGrowthRate" and key !="diamondUseGrowthRate" and key !="rechargeGrowthRate":
            print('{key}:{value}'.format(key = key , value = value))
    #print(response['data']['liveList'][0]['activityMoney'])
    if (response['data']['liveList'][0]['activityMoney']) == 0:
        print("liveList-activityMoney_Error")
    if (response['data']['liveList'][0]['cashout']) == 0:
        print("liveList-cashout_Error")
    if (response['data']['liveList'][0]['dataTime']) == 0:
        print("liveList-dataTime_Error")
    if (response['data']['liveList'][0]['diamondGift']) == 0:
        print("liveList-diamondGift_Error")
    if (response['data']['liveList'][0]['diamondRecharge']) == 0:
        print("liveList-diamondRecharge_Error")
    if (response['data']['liveList'][0]['diamondRechargeCount']) == 0:
        print("liveList-diamondRechargeCount_Error")
    if (response['data']['liveList'][0]['diamondUse']) == 0:
        print("liveList-diamondUse_Error")
    if (response['data']['liveList'][0]['recharge']) == 0:
        print("liveList-recharge_Error")
    else:
        print("日報表-直播數據(8)_Check OK")
# for gameList in (response['data']['gameList']):
    #     if (gameList.get('availableBetSum')) == 0:
    #         print('availableBetSum_Error')
    #     if (gameList.get('bet')) == 0:
    #         print('bet_Error')
    #     if (gameList.get('betUserCount')) == 0:
    #         print('betUserCount_Error')
    #     if (gameList.get('dataTime')) == 0:
    #         print('dataTime_Error')
    #     if (gameList.get('fsMoney')) == 0:
    #         print('fsMoney_Error')
    #     if (gameList.get('income')) == 0:
    #         print('income_Error')
    #     else:
    #         print("日報表-遊戲數據_Check OK")
    # for liveList in (response['data']['liveList']):
    #     print(type(liveList))
    #     # print(liveList.get('activityMoney'))
    #     if (liveList.get('activityMoney')) == 0:
    #         print('activityMoney_Error')
    #     if (liveList.get('cashout')) == 0:
    #         print('cashout_Error')
    #     if (liveList.get('dataTime')) == 0:
    #         print('dataTime_Error')
    #     if (liveList.get('diamondGift')) == 0:
    #         print('diamondGift_Error')
    #     if (liveList.get('diamondRecharge')) == 0:
    #         print('diamondRecharge_Error')
    #     if (liveList.get('diamondRechargeCount')) == 0:
    #         print('diamondRechargeCount_Error')
    #     if (liveList.get('diamondUse')) == 0:
    #         print('diamondUse_Error')
    #     if (liveList.get('recharge')) == 0:
    #         print('recharge_Error')
    #     else:
    #         print("日報表-直播數據(8)_Check OK")
    #print(response['liveList']['recharge'])
    #response1 =response.get("data",[])#第二層
    # print(response['gameList'],[])
    # print(response1[liveList])

    # response1 =response.get("data",['liveList'])#第二層
    # #print(response1)
    # key = response1.keys()
def gameBet():
    url = ' http://8.219.83.66:8088/admin/dataCenter/gameBet/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'endTime': date_endtime_stamp,
            'gameType':'',
            'openChannelId':'',
            'pageNum':'1',
            'pageSize':'10000',
            'pid':'',}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    #print(_data)
    # print(r)
    response = r.json()  # 轉json
    print('--------遊戲注單統計(6)+類型-波音彩票(6)--------')
    for key,value in response["totalData"].items():
        # if key !="":
            print('{key}:{value}'.format(key = key , value = value))
    if response["totalData"]["availableBetSum"] == 0:
        print("availableBetSum_Error")
    if response["totalData"]["betCount"] == 0:
        print("betCount_Error")
    if response["totalData"]["betSum"] == 0:
        print("betSum_Error")
    if response["totalData"]["income"] == 0:
        print("income_Error")
    if response["totalData"]["killRate"] == 0:
        print("killRate_Error")
    if response["totalData"]["ticketForPodcast"] == 0:
        print("ticketForPodcast_Error")
    else:
        print("遊戲注單統計(6)_Check OK")
    #print(response['data'][0])
    for key,value in response['data'][0].items():
         if key !="gameType" and key !="gameTypeName" and key !="pid" and key !="supplier" and key !="timezone":
            print('{key}:{value}'.format(key = key , value = value))
    if (response['data'][0]['availableBetSum']) == 0:
        print("波音彩票availableBetSum_Error")
    if (response['data'][0]['betCount']) == 0:
        print("波音彩票betCount_Error")
    if (response['data'][0]['betSum']) == 0:
        print("波音彩票betSum_Error")
    if (response['data'][0]['income']) == 0:
        print("波音彩票income_Error")
    if (response['data'][0]['killRate']) == 0:
        print("波音彩票killRate_Error")
    if (response['data'][0]['ticketForPodcast']) == 0:
        print("遊戲注單統計_波音彩票ticketForPodcast_Error")
    else:
        print("類型-波音彩票(6)_Check OK")

def gameBetDetail():
    url = 'http://8.219.83.66:8088/admin/dataCenter/gameBetDetail/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId':'',
            'country':'cn',
            'currency':'',
            'endTime': date_endtime_stamp,
            'openChannelId':'',
            'pageNum':'1',
            'pageSize':'20',
            'parm':'',
            'pid':'',}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    #print(_data)
    # print(r)
    response = r.json()  # 轉json
    # for i in response:
    #     print(i)
    #print(response)
    print('--------遊戲數據列表(5)+類型-動博體育(5)--------')
    for key,value in response["totalData"].items():
        if key !="tip":
            print('{key}:{value}'.format(key = key , value = value))
    if response["totalData"]["availableBetNum"] == 0:
        print("availableBetNum_Error")
    if response["totalData"]["betCount"] == 0:
        print("betCount_Error")
    if response["totalData"]["betNum"] == 0:
        print("betNum_Error")
    if response["totalData"]["income"] == 0:
        print("income_Error")
    if response["totalData"]["killRate"] == 0:
        print("killRate_Error")
    # if response["totalData"]["tip"] == 0:
    #     print("tip_Error")
    else:
        print("遊戲數據列表(5)_Check ok")
    #print(response["data"][9]["availableBetNum"])
    for key,value in response["data"][9].items():
        if key !="gameName" and key !="pid" and key !="supplier" and key !="tip":
            print('{key}:{value}'.format(key = key , value = value))
    if response["data"][9]["availableBetNum"] == 0:
        print("availableBetNum_Error")
    if response["data"][9]["betCount"] == 0:
        print("betCount_Error")
    if response["data"][9]["betNum"] == 0:
        print("betNum_Error")
    if response["data"][9]["income"] == 0:
        print("income_Error")
    if response["data"][9]["killRate"] == 0:
        print("killRate_Error")
    else:
        print("類型-動博體育(5)_Check ok")

if __name__== '__main__':
    #channels()
    # rechargeCashoutDiff()#數據總表
    # newRegCount()#數據總表
    # firstDayPayRate()#數據總表
    # agentData()#數據總表
    # gameData()#數據總表
    # podcastDiamond()#數據總表
    # diamondConsumption()#數據總表
    # profiles()#數據總表_會員財務數據-會員
    # online()#數據總表_會員財務數據-活躍
    # recharge() #數據總表_會員財務數據-首充/二充
    # bet_blocks() #數據總表_遊戲數據
    # live_blocks() #數據總表_遊戲數據
     businessReport() #經營報表
    # dailyReport() #日報表
    # gameBet() #遊戲注單列表
    # gameBetDetail() #遊戲數據列表

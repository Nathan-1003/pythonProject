import requests
import json
import base64
import hashlib
#import pytest

# pp部分
# ctrl ={
# app_info
# caipiao_bet
# cash_class
# cash
# fs_finally_config
# fs_finally_scheme
# game_list
# game_log
# game_money_log
# game_type
# tg
# user_payway
# vip
# }

# live 部分
# ctrl ={
# channel
# diamond_exchange
# diamond
# item
# payment_class
# payment
# recharge
# room
# ticket_log
# user
# }


# baseUrl = "https://reqres.in/"

# baseUrl = "http://8.219.58.126:10086"
ppbaseUrl = "http://8.219.58.126:10086"
livebaseUrl = "http://8.219.58.126:10086"

saltKey = "fd63b3e39a94acf8"

begin_time = "1660779600"
end_time = "1662528600"
tm = end_time

def genSignature(info):

    data = info + saltKey

    m = hashlib.md5()
    m.update(data.encode("utf-8"))

    return m.hexdigest()

def genInfo(dist):

    b = dist.encode("UTF-8")

    return base64.b64encode(b).decode('UTF-8')

def test_list_user():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user","begin_time":1654732800,"ctl":"user","end_time":1652486400,"page":1,"page_size":500,"tm":1654573070}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_fs_daily_stat():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_fs_daily_stat","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573190}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_tg_daily_bet_stat():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_tg_daily_bet_stat","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573348}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_tg_daily_fenhong_log():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_tg_daily_fenhong_log","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573698}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_pp_user():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_pp_user","begin_time":1654732800,"ctl":"user","end_time":1652486400,"page":1,"page_size":500,"tm":1654573793}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_pp_user_change_ids():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_pp_user_change_ids","ctl":"user","page":1,"page_size":500,"report_date":20220521,"tm":1654573910}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_pp_user_by_id():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_pp_user_by_id","ctl":"user","ids":"[1,2,3]","page":1,"page_size":500,"tm":1654574025}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["data"][0]["username"] == ""):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False
    
    if(response.status_code != 200):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert True

def test_list_user_extern():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user_extern","begin_time":1654732800,"ctl":"user","end_time":1652486400,"page":1,"page_size":500,"tm":1654574282}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200    
    
def test_list_user_extern_change_ids():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user_extern_change_ids","ctl":"user","page":1,"page_size":500,"report_date":202205041122,"tm":1654574450}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)
    
    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200
    
def test_list_user_extern_by_id():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user_extern_by_id", "ctl":"user", "ids":"[22762460, 23657643, 75020779]", "page":1, "page_size":500, "tm":1654678223}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["data"] == {}):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_diamond_log():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_diamond_log","begin_t":1654732800,"ctl":"diamond","end_t":1652486400,"oper_type":1,"page":1,"page_size":500,"tm":1654579557}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)

    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")


def test_get_online_podcast_count():

    path = "/open_api/proxy_api"

    dist = '{"act":"get_online_podcast_count","ctl":"room","tm":1654579750}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)

    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")
    
    if(response.json()["data"] == "0"):
        
        print("\n"+livebaseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_ctl_cash():

    path = "/open_api/proxy_api"

    dist = '{"act":"list","begin_time":1627309134,"ctl":"cash","end_time":1627309334,"tm":1654579845}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)

    if(response.json()["data"] == {}):

        print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_ctl_payment():

    path = "/open_api/proxy_api"

    # dist = '{"act":"list","begin_time":1662595200000,"ctl":"payment","end_time":1662728400000,"tm":1662728400}'
    dist = '{"act":"list","begin_time":' + begin_time + ',"ctl":"payment","end_time":' + end_time + ',"tm":'+ tm +'}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)
    
    #if(response.json()["data"][0]["pay_time"] == ""):
        
    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    # print(response.text+"\n")

    #   assert False

    # assert response.status_code == 200

def test_list_activity_log():

    path = "/open_api/proxy_api"
  
    # dist = '{"act":"list_activity_log","begin_time":1654617600,"ctl":"game_money_log","end_time":1654704000,"tm":1654580812}'
    dist = '{"act":"list_activity_log","begin_time":1662525000,"ctl":"game_money_log","end_time":1662528600,"tm":1662528600}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    #if(response.json()["data"] == {}):
        
    print("\n"+baseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

    #   assert False

    #ssert response.status_code == 200

def test_list_caipiao_bet():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_caipiao_bet","begin_time":'+begin_time+',"ctl":"caipiao_bet","end_time":'+end_time+',"page":1,"page_size":500,"tm":'+tm+'}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)
    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

    # if(response.json()["result"] == {}):
        
    #     print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    #     print(dist+"\n")
    #     print(response.text+"\n")

    #     assert False

    # assert response.status_code == 200

def test_list_ctl_channel():

    path = "/open_api/proxy_api"

    dist = '{"act":"list","ctl":"channel","tm":1654581128}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["result"][0]["channel_id"] == ""):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_exchange_log():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_exchange_log","begin_t":1651407548,"ctl":"diamond_exchange","end_t":1652962748,"page":1,"page_size":500,"tm":1654581407}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["result"] == {}):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_user_by_id():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user_by_id","ctl":"user","ids":"[1,2,3]","tm":1654581541}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["data"][0]["username"] == ""):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_game_log():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_game_log","begin_time":0,"ctl":"game_log","end_time":9999999999999999,"has_next":"0","page":1,"page_size":500,"tb_index":"2","tm":1654581706}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["result"][0]["user_id"] == ""):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200

def test_list_game_log2():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_game_log","begin_time":1662553803,"ctl":"game_log","end_time":1662557417,"has_next":"0","page":1,"page_size":500,"tb_index":"2","tm":1662557417}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    print("\n"+baseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")



def test_list_ticket_log():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_ticket_log","begin_time":1662535837,"ctl":"ticket_log","end_time":1662539438,"page":1,"page_size":500,"tm":1662539438}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    print("\n"+baseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

if name == '__main__':
    test_get_online_podcast_count()



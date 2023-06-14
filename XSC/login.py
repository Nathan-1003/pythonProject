import requests
import json

def login():
    url = 'https://miniapp.qcgamer.com/admin/user/login'
    headers = {"content-type": "application/json"}
    data = '{"username":"admin","password":"12345678","validation":"666666"}'
    r = requests.post(url, headers=headers, data=data)
    # print(r.text) #成功登入
    t = json.loads(r.text)#提取response中的token取用
    # print(t)
    token = t['data']['loginVO']['jwtToken']
    print(token)

    # url = 'Request URL: https://miniapp.qcgamer.com/admin/version/add'
    # headers = {"Content-Type": "application/json","Authorization": token}
    # data ='{"appName": "ddddd","versionName": "1.00","isEnabled": false,"fileMd5": "e187bcd96026d32fc9fe7e6bb99b2f43","filename": "測試用照片一張.jpeg.zip","subappName": "1234"}'
    # r = requests.post(url, headers=headers, data=data)
    # print(r.text)
    #



if __name__== '__main__':
    login()


import requests
import json

def test_logging():
    url = 'https://www.qcgamer.com/server/system/getSettlements?gameId=texas&page=1&pageSize=10&token=livestreamlivestreamlivestream12'
    r = requests.get(url)
    print(r.text)
    # for key,value in (r.json).items():
    #      print('{key}:{value}'.format(key=key, value=value))



if __name__== '__main__':
    test_logging()




import urllib.request as req
import ssl

url = "https://www.kkday.com/zh-tw"
context = ssl._create_unverified_context()


request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
})


with req.urlopen(request, context=context) as response:
    data = response.read().decode("utf-8")

print(data)
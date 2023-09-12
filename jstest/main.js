import execjs

# 指定絕對路徑來讀取 js 檔案
with open('/Users/menglungtsai/pythonProject/gamessc/ssc/35754.js', 'r') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

result = ctx.call('judge', [9, 2, 3, 4, 5])
print(result)  # 1 或 -1
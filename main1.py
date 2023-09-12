import execjs

# 讀取JavaScript代碼
with open('/Users/menglungtsai/pythonProject/1.js', 'r') as f:
    js_code = f.read()

# 編譯JavaScript代碼
ctx = execjs.compile(js_code)

# 調用JavaScript函數
result = ctx.call('add', 2, 3)
print(result)  # 5

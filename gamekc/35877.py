import execjs
import random
from colorama import Fore, Style 

# 讀取 JavaScript 
with open('/Users/menglungtsai/pythonProject/gamekc/kcjs/35877_冠军_10.js', 'r') as f:
    js_code = f.read()

# 編譯 JavaScript 
ctx = execjs.compile(js_code)

# 定義判斷
def judge(bets):
    return ctx.call('judge', bets)

# 初始化统计变量
count_1 = 0
count_minus_1 = 0

# 生成 10 組不重複號碼並判斷
for i in range(500):
    combo = random.sample(range(1, 11), 10)
    
    # 呼叫判斷函數並傳遞生成的號碼
    result = judge(combo)

    # 輸出判斷結果
    s = sum(combo[:2])
    if result == 1:
        count_1 += 1
        print(f"{Fore.RED}組合 {i + 1}: {combo}, 冠軍{combo[0]},結果: {result}{Style.RESET_ALL}")
    else:
        count_minus_1 += 1
        print(f"組合 {i + 1}: {combo}, 冠軍{combo[0]},結果: {result}{Style.RESET_ALL}")

# 輸出統計結果
print(f"1 的組數: {count_1}")
print(f"-1 的組數: {count_minus_1}")
print(f"{Fore.RED}35877_冠军_10")

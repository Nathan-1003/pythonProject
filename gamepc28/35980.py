import execjs
import random
from colorama import Fore, Style 

# 讀取 JavaScript 
with open('/Users/menglungtsai/pythonProject/gamepc28/pc28js/35980_和值_12.js', 'r') as f:
    js_code = f.read()

# 編譯 JavaScript 
ctx = execjs.compile(js_code)

# 定義判斷
def judge(bets):
    return ctx.call('judge', bets)

count = 0
count_1 = 0
count_minus_1 = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            total = i + j + k
            combo =[i, j, k]
            #print("當次帶入參數組合:", combo, "總和:", total)
            result = judge(combo)
            if result == 1:
                count_1 +=1
                print(Fore.RED + "當次帶入參數組合:", combo, "總和:", total,"結果:", str(result) + Style.RESET_ALL)
            else:
                count_minus_1 +=1
                print("當次帶入參數組合:", combo, "總和:", total, "結果:", str(result))

print("總共生成組合數量:", count)
print(f"{Fore.RED}結果1的次數:", count_1)
print("結果-1的次數:", count_minus_1)
print(f"{Fore.RED}35980_和值_12")

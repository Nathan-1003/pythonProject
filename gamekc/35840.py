import execjs
import random
from colorama import Fore, Style 

# 讀取 JavaScript 
with open('/Users/menglungtsai/pythonProject/gamekc/kcjs/35840_冠亚和两面_小.js', 'r') as f:
    js_code = f.read()

# 編譯 JavaScript 
ctx = execjs.compile(js_code)

# 定義判斷
def judge(bets):
    return ctx.call('judge', bets)

# 初始化统计变量
count_1 = 0
count_minus_1 = 0

# 生成 
for i in range(500):
    combo = random.sample(range(1, 11), 10)
    
# 计算第一位和第二位的和
    s = combo[0] + combo[1]

# 调用判断函数并传递生成的数字组合
    result = judge([s] + combo)

    # 输出判断结果
    if result == 1:
        count_1 += 1
        print(f"{Fore.RED}組合 {i + 1}: {combo}, 冠亞總和{s}, 結果: {result}{Style.RESET_ALL}")
    else:
        count_minus_1 += 1
        print(f"组合 {i + 1}: {combo}, 冠亚總和：{s}, 结果：{result}")

print(f"1 的组数: {count_1}")
print(f"-1 的组数: {count_minus_1}")
print(f"{Fore.RED} 冠亚和两面_小，冠亚總和小於等於11")
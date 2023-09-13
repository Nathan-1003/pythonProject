import execjs
import random
from colorama import Fore, Style 

#讀取 JavaScript 
with open('/Users/menglungtsai/pythonProject/gamessc/ssc/35772_五球两面_单.js', 'r') as f:
    js_code = f.read()

#編譯 JavaScript 
ctx = execjs.compile(js_code)

#定義判斷
def judge(bets):
    return ctx.call('judge', bets)

#生成
def generate_lottery_numbers(num_sets):
    lottery_numbers = set()

    while len(lottery_numbers) < num_sets:
        numbers = tuple(random.sample(range(10), 5))
        lottery_numbers.add(numbers)

    return list(lottery_numbers)

lottery_sets = generate_lottery_numbers(300)
count_1 = 0
count_minus_1 = 0

for i in range(300):
    result = judge(list(lottery_sets[i]))
    if result == 1:
        count_1 += 1
        print(f"{Fore.RED}組合 {i + 1}: {lottery_sets[i]} 結果: {result}{Style.RESET_ALL}")
    else:
        count_minus_1 += 1

    # 打印結果為-1的組合
    if result == -1:
        print(f"組合 {i + 1}: {lottery_sets[i]} 結果: {result}")

print(f"1 的組數: {count_1}")
print(f"-1 的組數: {count_minus_1}")

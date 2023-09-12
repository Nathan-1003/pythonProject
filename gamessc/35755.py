#ssc/35755_一球两面_小.js
import random
from colorama import Fore, Style

def judge(bets):
    if len(bets) != 5:
        return -1

    parsed_bets = [int(item) for item in bets]

    for num in parsed_bets:
        if num < 0 or num > 9:
            return -1

    # 第一球小於等於4即為小
    ball = parsed_bets[0]
    if ball <= 4:
        return 1

    return -1

def generate_lottery_numbers(num_sets):
    lottery_numbers = set()

    while len(lottery_numbers) < num_sets:
        numbers = tuple(random.sample(range(10), 5))
        lottery_numbers.add(numbers)

    return list(lottery_numbers)

lottery_sets = generate_lottery_numbers(300)
count_1 = 0
count_minus_1 = 0

# 判定每组号码并统计
for i in range(300):
    result = judge(list(lottery_sets[i]))
    if result == 1:
        count_1 += 1
        # 使用红色字体打印结果为1的组合
        print(f"{Fore.RED}组合 {i + 1}: {lottery_sets[i]} 结果: {result}{Style.RESET_ALL}")
    else:
        count_minus_1 += 1

    # 打印结果为-1的组合
    if result == -1:
        print(f"组合 {i + 1}: {lottery_sets[i]} 结果: {result}")

print(f"1 的组数: {count_1}")
print(f"-1 的组数: {count_minus_1}")

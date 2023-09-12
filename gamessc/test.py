#source myenv/bin/activate
import random 

def generate_lottery_numbers(num_sets):
    lottery_numbers = set()

    while len(lottery_numbers) < num_sets:
        numbers = tuple(random.sample(range(10), 5))
        lottery_numbers.add(numbers)

    return list(lottery_numbers)

lottery_sets = generate_lottery_numbers(30)


# 格式化打印每组号码
formatted_lottery_sets = [",".join(map(str, numbers)) for numbers in lottery_sets]
print("[" + "],[".join(formatted_lottery_sets) + "]")





import random
from colorama import Fore, Style

def judge(bets):
    if len(bets) != 5:
        return -1
    
    parsed_bets = [int(item) for item in bets]

    for num in parsed_bets:
        if num < 0 or num > 9:
            return -1

    # 第一球大於等於5即為大
    ball = parsed_bets[0]
    if ball >= 5:
        return 1

    return -1

def generate_lottery_numbers(num_sets):
    lottery_numbers = set()

    while len(lottery_numbers) < num_sets:
        numbers = tuple(random.sample(range(10), 5))
        lottery_numbers.add(numbers)

    return list(lottery_numbers)

lottery_sets = generate_lottery_numbers(500)

# 初始化统计变量
count_1 = 0
count_minus_1 = 0

# 判定每组号码并统计
for i in range(500):
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

# 格式化打印每组号码
formatted_lottery_sets = [",".join(map(str, numbers)) for numbers in lottery_sets]
print("[" + "],[".join(formatted_lottery_sets) + "]")

print(f"1 的组数: {count_1}")
print(f"-1 的组数: {count_minus_1}")

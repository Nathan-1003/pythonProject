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


import random

def generate_lottery_numbers(num_sets):
    lottery_numbers = []

    while len(lottery_numbers) < num_sets:
        numbers = tuple(random.choices(range(10), k=5))
        lottery_numbers.append(numbers)

    return lottery_numbers

if __name__ == "__main__":
    num_sets = 10  # 設定要生成的彩票組數
    lottery_sets = generate_lottery_numbers(num_sets)
    print(lottery_sets)
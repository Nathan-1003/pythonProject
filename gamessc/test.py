def generate_lottery_numbers(num_sets):
    lottery_numbers = []

    while len(lottery_numbers) < num_sets:
        numbers = tuple(random.choices(range(10), k=5))
        lottery_numbers.append(numbers)

    return lottery_numbers
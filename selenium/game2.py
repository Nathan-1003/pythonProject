import random
from colorama import Fore, Style

def lottery_numbers():
    count = 0
    results = []
    while count < 1000:
        first_six = random.sample(range(1, 50), 6)
        seventh = random.choice([num for num in range(1, 50) if num not in first_six])
        result = first_six + [seventh]
        results.append(result)
        count += 1
    return results
def judge(bets):
    if len(bets) != 7:
        return -1
    parsed_bets = [int(item) for item in bets]
    for bet in parsed_bets:
        if not (1 <= bet <= 49):
            return -1
    special = parsed_bets[6]
    if special == 1:
        return 1
    return -1
combo = lottery_numbers()
#print(combo)    #列出300組
for numbers in combo:
    result = judge(numbers)
    if result == 1:
        print(Fore.RED + f"{numbers} 結果: {result}" + Style.RESET_ALL)
    else:
        print(f"{numbers} 結果: {result}")


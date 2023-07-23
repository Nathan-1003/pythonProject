import random
from colorama import Fore, Style

def judge1(bets):
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
def lot35606():
    count = 0
    results = []
    while count < 500:
        six = random.sample(range(1, 50), 6)
        seventh = random.choice([num for num in range(1, 50) if num not in six])
        result = six + [seventh]
        results.append(result)
        count += 1
        # 判斷並輸出結果
        if judge1(result) == 1:
            print(Fore.RED + f"{result} 結果: 1" + Style.RESET_ALL)
        else:
            print(f"{result} 結果: -1")
    print("生成組數:", count)
    return results

def judge1(bets):
    if len(bets) != 7:
        return -1
    parsed_bets = [int(item) for item in bets]
    for bet in parsed_bets:
        if not (1 <= bet <= 49):
            return -1
    special = parsed_bets[6]
    if special == 2:
        return 1
    return -1
def lot35607():
    count = 0
    results = []
    while count < 500:
        six = random.sample(range(1, 50), 6)
        seventh = random.choice([num for num in range(1, 50) if num not in six])
        result = six + [seventh]
        results.append(result)
        count += 1
        # 判斷並輸出結果
        if judge1(result) == 1:
            print(Fore.RED + f"{result} 結果: 1" + Style.RESET_ALL)
        else:
            print(f"{result} 結果: -1")
    print("生成組數:", count)
    return results

def judge1(bets):
    if len(bets) != 7:
        return -1
    parsed_bets = [int(item) for item in bets]
    for bet in parsed_bets:
        if not (1 <= bet <= 49):
            return -1
    special = parsed_bets[6]
    if special == 3:
        return 1
    return -1
def lot35608():
    count = 0
    results = []
    while count < 500:
        six = random.sample(range(1, 50), 6)
        seventh = random.choice([num for num in range(1, 50) if num not in six])
        result = six + [seventh]
        results.append(result)
        count += 1
        # 判斷並輸出結果
        if judge1(result) == 1:
            print(Fore.RED + f"{result} 結果: 1" + Style.RESET_ALL)
        else:
            print(f"{result} 結果: -1")
    print("生成組數:", count)
    return results















if __name__ == "__main__":
    #lot35606()     #六合彩特碼1
    #lot35607()     #六合彩特碼2
    lot35608()
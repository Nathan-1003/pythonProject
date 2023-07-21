from colorama import Fore, Style

#快三_大小_大
def judge_35708(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    if parsed_bets[0] == parsed_bets[1] == parsed_bets[2]:
        return -1

    total_sum = sum(parsed_bets)

    if 11 <= total_sum < 18:
        return 1

    return -1
def bet_35708():
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35708(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                else:
                    print("結果:", str(result))

    print("總共生成組合數量:", count)

#快三_大小_小
def judge_35709(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    if parsed_bets[0] == parsed_bets[1] == parsed_bets[2]:
        return -1

    total_sum = sum(parsed_bets)

    if 4 <= total_sum < 11:
        return 1

    return -1
def bet_35709():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35709(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_大小_單
def judge_35710(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)
    check_numbers = [3, 5, 7, 9, 11, 13, 15, 17]

    if total_sum in check_numbers:
        return 1

    return -1
def bet_35710():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35710(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_大小_雙
def judge_35711(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)
    check_numbers = [4, 6, 8, 10, 12, 14, 16, 18]

    if total_sum in check_numbers:
        return 1

    return -1
def bet_35711():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35711(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_4點
def judge_35712(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 4:
        return 1

    return -1
def bet_35712():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35712(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_5點
def judge_35713(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 5:
        return 1

    return -1
def bet_35713():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35713(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_6點
def judge_35714(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 6:
        return 1

    return -1
def bet_35714():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35714(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_7點
def judge_35715(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 7:
        return 1

    return -1
def bet_35715():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35715(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_8點
def judge_35716(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 8:
        return 1

    return -1
def bet_35716():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35716(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_9點
def judge_35717(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 9:
        return 1

    return -1
def bet_35717():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35717(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_10點
def judge_35718(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 10:
        return 1

    return -1
def bet_35718():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35718(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_11點
def judge_35719(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 11:
        return 1

    return -1
def bet_35719():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35719(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_12點
def judge_35720(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 12:
        return 1

    return -1
def bet_35720():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35720(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_13點
def judge_35721(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 13:
        return 1

    return -1
def bet_35721():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35721(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_14點
def judge_35722(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 14:
        return 1

    return -1
def bet_35722():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35722(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_15點
def judge_35723(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 15:
        return 1

    return -1
def bet_35723():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35723(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_16點
def judge_35724(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 16:
        return 1

    return -1
def bet_35724():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35724(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_17點
def judge_35725(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 17:
        return 1

    return -1
def bet_35725():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35725(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)

#快三_總和_18點
def judge_35726(bets):
    if len(bets) != 3:
        return -1

    parsed_bets = [int(item) for item in bets]

    for bet in parsed_bets:
        if bet <= 0 or bet >= 7:
            return -1

    total_sum = sum(parsed_bets)

    if total_sum == 18:
        return 1

    return -1
def bet_35726():
    count = 0
    count_minus_one = 0
    count_one = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                total = i + j + k
                combo = f"{i},{j},{k}"
                print("當次帶入參數組合:", combo, "合計:", total)
                count += 1

                bets_array = combo.split(',') #將 combo 字串以逗號作為分隔符，分割成一個包含三個子字串的列表
                bets_array = [int(bet) for bet in bets_array] #將每個子字串轉換成整數。這個列表推導式將對 bets_array 中的每個元素 bet 執行 int(bet)
                result = judge_35726(bets_array) #將列表 bets_array 作為參數傳遞給 judge_35712 函式，並將返回的結果賦值給變數 result

                if result == 1:
                    print(Fore.RED + "結果:", str(result) + Style.RESET_ALL)
                    count_one += 1
                else:
                    print("結果:", str(result))
                    count_minus_one += 1

    print("總共次數:", count)
    print("結果為 -1(未中獎) 的次數:", count_minus_one)
    print("結果為 1(中獎) 的次數:", count_one)



[[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5],[1,1,6],[1,2,1],[1,2,2],[1,2,3],[1,2,4],[1,2,5],[1,2,6],[1,3,1],[1,3,2],[1,3,3],[1,3,4],[1,3,5],[1,3,6],[1,4,1],[1,4,2],[1,4,3],[1,4,4],[1,4,5],[1,4,6],[1,5,1],[1,5,2],[1,5,3],[1,5,4],[1,5,5],[1,5,6],[1,6,1],[1,6,2],[1,6,3],[1,6,4],[1,6,5],[1,6,6],[2,1,1],[2,1,2],[2,1,3],[2,1,4],[2,1,5],[2,1,6],[2,2,1],[2,2,2],[2,2,3],[2,2,4],[2,2,5],[2,2,6],[2,3,1],[2,3,2],[2,3,3],[2,3,4],[2,3,5],[2,3,6],[2,4,1],[2,4,2],[2,4,3],[2,4,4],[2,4,5],[2,4,6],[2,5,1],[2,5,2],[2,5,3],[2,5,4],[2,5,5],[2,5,6],[2,6,1],[2,6,2],[2,6,3],[2,6,4],[2,6,5],[2,6,6],[3,1,1],[3,1,2],[3,1,3],[3,1,4],[3,1,5],[3,1,6],[3,2,1],[3,2,2],[3,2,3],[3,2,4],[3,2,5],[3,2,6],[3,3,1],[3,3,2],[3,3,3],[3,3,4],[3,3,5],[3,3,6],[3,4,1],[3,4,2],[3,4,3],[3,4,4],[3,4,5],[3,4,6],[3,5,1],[3,5,2],[3,5,3],[3,5,4],[3,5,5],[3,5,6],[3,6,1],[3,6,2],[3,6,3],[3,6,4],[3,6,5],[3,6,6],[4,1,1],[4,1,2],[4,1,3],[4,1,4],[4,1,5],[4,1,6],[4,2,1],[4,2,2],[4,2,3],[4,2,4],[4,2,5],[4,2,6],[4,3,1],[4,3,2],[4,3,3],[4,3,4],[4,3,5],[4,3,6],[4,4,1],[4,4,2],[4,4,3],[4,4,4],[4,4,5],[4,4,6],[4,5,1],[4,5,2],[4,5,3],[4,5,4],[4,5,5],[4,5,6],[4,6,1],[4,6,2],[4,6,3],[4,6,4],[4,6,5],[4,6,6],[5,1,1],[5,1,2],[5,1,3],[5,1,4],[5,1,5],[5,1,6],[5,2,1],[5,2,2],[5,2,3],[5,2,4],[5,2,5],[5,2,6],[5,3,1],[5,3,2],[5,3,3],[5,3,4],[5,3,5],[5,3,6],[5,4,1],[5,4,2],[5,4,3],[5,4,4],[5,4,5],[5,4,6],[5,5,1],[5,5,2],[5,5,3],[5,5,4],[5,5,5],[5,5,6],[5,6,1],[5,6,2],[5,6,3],[5,6,4],[5,6,5],[5,6,6],[6,1,1],[6,1,2],[6,1,3],[6,1,4],[6,1,5],[6,1,6],[6,2,1],[6,2,2],[6,2,3],[6,2,4],[6,2,5],[6,2,6],[6,3,1],[6,3,2],[6,3,3],[6,3,4],[6,3,5],[6,3,6],[6,4,1],[6,4,2],[6,4,3],[6,4,4],[6,4,5],[6,4,6],[6,5,1],[6,5,2],[6,5,3],[6,5,4],[6,5,5],[6,5,6],[6,6,1],[6,6,2],[6,6,3],[6,6,4],[6,6,5],[6,6,6]]

if __name__ == "__main__":
    #bet_35708()    #快三_大小_大
    #bet_35709()    #快三_大小_小
    #bet_35710()    #快三_大小_單
    #bet_35711()    #快三_大小_雙
    #bet_35712()    #快三_總和_4點
    #bet_35713()    #快三_總和_5點
    #bet_35714()    #快三_總和_6點
    #bet_35715()    #快三_總和_7點
    #bet_35716()    #快三_總和_8點
    #bet_35717()    #快三_總和_9點
    #bet_35718()    #快三_總和_10點
    #bet_35719()    #快三_總和_11點
    #bet_35720()    #快三_總和_12點
    bet_35721()    #快三_總和_13點
    # bet_35722()    #快三_總和_14點
    # bet_35723()    #快三_總和_15點
    # bet_35724()    #快三_總和_16點
    # bet_35725()    #快三_總和_17點







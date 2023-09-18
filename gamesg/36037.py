import execjs
import random
from colorama import Fore, Style 

# 讀取 JavaScript 
with open('/Users/menglungtsai/Downloads/judge-main-sg/sg/36037_庄闲_闲.js', 'r') as f:
    js_code = f.read()

# 編譯 JavaScript 
ctx = execjs.compile(js_code)

# 定义牌号映射表
card_mapping = {
    1: "方塊1", 2: "梅花1", 3: "愛心1", 4: "黑桃1",
    5: "方塊2", 6: "梅花2", 7: "愛心2", 8: "黑桃2",
    9: "方塊3", 10: "梅花3", 11: "愛心3", 12: "黑桃3",
    13: "方塊4", 14: "梅花4", 15: "愛心4", 16: "黑桃4",
    17: "方塊5", 18: "梅花5", 19: "愛心5", 20: "黑桃5",
    21: "方塊6", 22: "梅花6", 23: "愛心6", 24: "黑桃6",
    25: "方塊7", 26: "梅花7", 27: "愛心7", 28: "黑桃7",
    29: "方塊8", 30: "梅花8", 31: "愛心8", 32: "黑桃8",
    33: "方塊9", 34: "梅花9", 35: "愛心9", 36: "黑桃9",
    37: "方塊10", 38: "梅花10", 39: "愛心10", 40: "黑桃10",
    41: "方塊11", 42: "梅花11", 43: "愛心11", 44: "黑桃11",
    45: "方塊12", 46: "梅花12", 47: "愛心12", 48: "黑桃12",
    49: "方塊13", 50: "梅花13", 51: "愛心13", 52: "黑桃13",
}

# 定义判断函数，根据规则判断胜负
def judge(bets):
    if len(bets) != 8:
        return -1

    for num in bets:
        if num < 1 or num > 52:
            return -1

    result_xian = bets[3] % 10
    result_zhuang = bets[7] % 10

    return result_xian, result_zhuang

# 生成 9 个不重复的数字（范围：1-52），用整数表示牌号
poker_cards = list(range(1, 53))
bets = random.sample(poker_cards, 8)

# 计算123的总和并取个位数，处理J、Q、K映射为10
total_123 = (bets[0] % 10 + bets[1] % 10 + bets[2] % 10) % 10
bets[0] = card_mapping[bets[0]]
bets[1] = card_mapping[bets[1]]
bets[2] = card_mapping[bets[2]]

# 计算567的总和并取个位数，处理J、Q、K映射为10
total_567 = (bets[4] % 10 + bets[5] % 10 + bets[6] % 10) % 10
bets[4] = card_mapping[bets[4]]
bets[5] = card_mapping[bets[5]]
bets[6] = card_mapping[bets[6]]

# 输出生成的扑克牌标识和判断结果
print(f"閑牌: {bets[:3]}, 總和為{total_123}, 莊牌: {bets[4:7]}, 總和為{total_567}")


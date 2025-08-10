# เขียนฟังกชันแกปญหา Coin Change Problem: กําหนดเหรียญหลายชนิดและจํานวนเงินเปาหมาย ใหหาจํานวนวิธี
# ทั้งหมดที่สามารถรวมเหรียญใหไดเทากับเปาหมาย
def count_ways_to_make_amount(coin_types, target_amount):
    ways = [0] * (target_amount + 1)
    ways[0] = 1  

    for coin in coin_types:
        for amount in range(coin, target_amount + 1):
            ways[amount] += ways[amount - coin]
    return ways[target_amount]

if __name__ == "__main__":
    available_coins = [2, 5, 10]
    goal = 20
    print("จำนวนวิธีรวมเหรียญให้ได้", goal, "บาท คือ:", count_ways_to_make_amount(available_coins, goal))

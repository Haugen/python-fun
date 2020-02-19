plus1 = [2, 3, 4, 5, 6]
zero = [7, 8, 9]
minus1 = [10, "J", "Q", "K", "A"]
allCards = plus1 + zero + minus1

def count(cards):
    if type(cards) != list: return
    if len(cards) == 0: return 0
    count = 0

    for card in cards:
        if card in plus1:
            count += 1
            continue
        if card in minus1:
            count -= 1
            continue

count([5, 9, 10, 3, "J", "A", 4, 8, 5]) # 1
count(["A", "A", "K", "Q", "Q", "J"]) # -6
count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) # 5
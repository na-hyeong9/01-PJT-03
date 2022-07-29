import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for i in range(1,T + 1):
    card = input()
    card_1 = str(card.replace('-',''))
    start = ('3', '4', '5', '6', '9')
    for j in card_1:
        if j in start and len(card_1) == 16:
            print(f'#{i} 1')
            break
        else:
            print(f'#{i} 0')
            break
        

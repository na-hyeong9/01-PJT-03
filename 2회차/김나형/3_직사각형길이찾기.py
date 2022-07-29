from re import L
import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for i in range(1, T + 1):
    line = list(map(int, input().split()))
    
    line_1 = set(line)
    
    for j in line_1:
        if line.count(j) == 1 or line.count(j) == 3:
            print(f'#{i} {j}')
    
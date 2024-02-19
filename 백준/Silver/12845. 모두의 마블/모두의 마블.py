import sys
input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))
level.sort(reverse=True)

gold = 0

for i in range(1,len(level)):
    gold += level[0] + level[i]

print(gold)
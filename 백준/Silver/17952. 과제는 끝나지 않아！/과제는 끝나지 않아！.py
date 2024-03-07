import sys
input = sys.stdin.readline

n = int(input())
score = []
work = [] 

for _ in range(n):
    row = list(map(int, input().split()))

    if row[0]==1:
        work.append([row[1], row[2]])
    else:
        pass
    
    if work:
        work[-1][-1] -= 1
        if work[-1][-1] == 0:
            score.append(work[-1][0])
            work.pop()

print(sum(score))
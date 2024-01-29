import sys
input = sys.stdin.readline

n,c = map(int, input().split())
term = [0]*(c+1) #폭죽 시간 배열
for i in range(n):
    time = int(input().strip())
    if time==1: 
        print(c)
        quit()
    for j in range(time, c+1, time): 
        term[j] = 1 #폭죽 터질때
print(sum(term))
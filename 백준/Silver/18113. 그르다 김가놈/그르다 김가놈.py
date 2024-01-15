import sys
input = sys.stdin.readline
n, k, M = map(int, input().split()) #김밥의 개수, 꼬다리의 길이, 김밥조각의 최소개수

arr=[]
for i in range(n):
    total = int(input())
    if(total>2*k):
        body = total-(2*k)
        arr.append(body)
    elif(total > k and total < 2*k):
        arr.append(total-k)

if len(arr) == 0:
    print(-1)
    exit(0)

P = -1 #김밥 조각의 최대 길이
l,r = 1,max(arr) #김밥 조각 길이 범위: 1~r

#이분탐색
while l <= r:

    m = (l+r)//2 #조각 김밥의 길이-중간값
    piece = sum([i//m for i in arr]) #가능한 김밥을 길이 m으로 나눴을 때 개수

    if piece < M: #개수가 부족하면 길이를 줄여야 함
        r = m-1
    else:
        l = m+1
        P = m

print(P)
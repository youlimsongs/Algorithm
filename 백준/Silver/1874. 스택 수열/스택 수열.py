from collections import deque

n = int(input())
num=[]
for i in range(n):
    num.append(int(input()))

que = deque()
que.append(0)
# print(que)
answer=[]
idx=0
cnt=1

while(idx < n and cnt < n+2):
    if que[len(que)-1] != num[idx]:
        que.append(cnt)
        answer.append("+")
        cnt+=1
    else:
        que.pop()
        answer.append("-")
        idx += 1
    
    # print(que)
    

if len(que)==1:
    for n in answer:
        print(n)
else:
    print("NO")
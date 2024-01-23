import sys
input = sys.stdin.readline

tmp=[]
n = int(input().strip())
answer = (list(input().strip().split(" ")))
check = (list(input().strip().split(" ")))

for i in range(len(check)):
    for j in range(len(answer)):
        if(answer[j]==check[i]):
            tmp.append(j)

# print(tmp)

res=0
for i in range(len(tmp)):
    for j in range(i+1, len(tmp)):
        if( tmp[i]<tmp[j]): res+=1

print(str(res)+"/"+str(n*(n-1)//2))
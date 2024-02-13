n = int(input())
size = list(map(int, input().split()))
cnt = 0 
temp=[]
doll = []

size.sort()

for i in range(n):
    temp.append(size[i]) 
    # print(temp)
    doll.append(temp)
    temp=[]

# print(doll)

for i in range(n):
    for j in range(i+1, n):
        if(doll[i][0] < doll[j][0] and len(doll[j])==1):
            cnt+=1
            doll[j].append(doll[i])
            doll[i]=0
            break

# print(doll)
# print(cnt)

print(len(doll)-cnt)
res=1

for i in range(3):
    num = int(input())
    res *= num

for i in range(0,10): 
    cnt = str(res).count(str(i))
    print(cnt)
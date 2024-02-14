n = int(input())
a, b,c =0, 0, 0
cnt=0

for a in range(1, n//2+1):
        for b in range(1, n):
            for c in range(b+2,n):
                if 2*a + b + c == n:
                    cnt += 1
        
if(cnt == 0):
    print(0)
else:
    print(cnt)
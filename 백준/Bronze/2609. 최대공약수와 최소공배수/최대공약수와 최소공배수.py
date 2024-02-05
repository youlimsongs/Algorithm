import sys
input = sys.stdin.readline

def gcd(a, b):
    while(b>0):
        a, b = b, a%b
    return a

a,b = map(int, input().split())
if(a<b):
    tmp=a
    a=b
    b=tmp
    
print(gcd(a,b))
print(a*b//gcd(a,b))
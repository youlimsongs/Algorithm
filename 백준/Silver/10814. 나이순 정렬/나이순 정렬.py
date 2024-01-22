import sys
input = sys.stdin.readline

n =int(input().strip())
total = []

for i in range(n):
    total.append(list((input().split())))

for i in sorted(total,key=lambda x : int(x[0])):
    print(i[0],i[1])
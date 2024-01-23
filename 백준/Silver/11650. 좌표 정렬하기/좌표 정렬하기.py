import sys
input = sys.stdin.readline

n =int(input().strip())
num = []
for i in range(n):
    num.append(list(map(int, input().split(" "))))

res = sorted(num, key=lambda k : (k[0],k[1]))
for i in range(n):
    print(res[i][0], res[i][1])
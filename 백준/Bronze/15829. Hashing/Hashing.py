l = int(input())
str = input().strip()

r, M = 31, 1234567891

# print(ord("a"))
res = 0
for i in range(l):
    s = ord(str[i]) - 96
    res += s * (r**i) % M

print(res)
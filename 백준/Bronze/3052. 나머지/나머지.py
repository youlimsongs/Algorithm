prev =[]
cnt =0

for i in range(10):
    num = int(input())
    res = num % 42

    prev.append(res)

print(len(list(set(prev))))
import sys

cnt = []
year = []
name = []
idx = 0

for i in range(3):
    data = sys.stdin.readline().split()
    cnt.append(int(data[0]))
    year.append(int(data[1])%100)
    name.append(str(data[2]))

sorted_idx = sorted(range(len(cnt)), key=lambda k: cnt[k], reverse=True)

year.sort()
for i in range(3):
    print(year[i],end='')

print()

for i in range(3):
    sorted_name = name[sorted_idx[i]]
    print(sorted_name[0], end='')
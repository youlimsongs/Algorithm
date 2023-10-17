n = int(input())
for i in range(n):
    repeat, str = input().split()
    repeat = int(repeat)
    for j in str:
        print(j*repeat, end="")
    print()
max = 0

for i in range(9):
    val = int(input())
    if(val>max):
        max=val
        index = i

print(max)
print(index+1)
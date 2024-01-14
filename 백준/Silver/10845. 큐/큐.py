import sys
input = sys.stdin.readline

n = int(input())
queue = []

for i in range(n):
    line = input().split()

    if line[0] =='push': queue.append(line[1])
    elif line[0] =='pop':
        if(queue): print(queue.pop(0))
        else: print(-1)
    
    elif line[0] == 'size': print(len(queue))
    elif line[0] == 'empty':
        if len(queue) == 0 : print(1)
        else: print(0)
    elif line[0] == 'front':
        if len(queue) != 0 : print(queue[0])
        else: print(-1)
    elif line[0] == 'back':
        if len(queue) != 0 : print(queue[-1])
        else: print(-1)
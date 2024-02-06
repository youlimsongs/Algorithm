import sys
input = sys.stdin.readline

group = 1

while(1):
    name = []
    mes = [] 
    target= -1

    n = int(input())
    if(n==0):
        break

    for i in range(n):
        per = list(input().split())
        name.append(per[0])
        mes.append(per[1:])

    # print(mes)
        
    print("Group", group)

    for i in range(len(mes)):   
        for j in range(len(mes[i])):
            if(mes[i][j]=='N'):
                target = (i+(len(mes)-1-j))% n
                # print(target)
                print(name[target]+" was nasty about "+name[i])
        
    if(target==-1):
        print("Nobody was nasty")
    print("")
    group+=1
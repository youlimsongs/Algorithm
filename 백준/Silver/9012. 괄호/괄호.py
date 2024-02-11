import sys
input = sys.stdin.readline

t = int(input().strip())
queue = []

for i in range(t):
    str = input().strip()
    idx=-1
    queue=[]
    res=0

    for s in str:
        if(len(queue)==0):
            if(s=='('):
                queue.append(s)
                idx += 1
                # print("1번",queue)
                # print("1번",idx)
            else:
                print('NO')
                res=-1
                # print("2번",queue)
                # print("2번",idx)
                break
            

        elif queue[idx]=='(' and s==')' :
            queue.pop()
            idx -= 1
            # print("3번",queue)
            # print("3번",idx)

        else:
            queue.append(s)
            idx += 1
            # print("4번",queue)
            # print("4번",idx)

        # print(queue)
        
    if len(queue) == 0 and res==0:
        print('YES')
    elif len(queue) != 0 and res==0:
        print('NO')
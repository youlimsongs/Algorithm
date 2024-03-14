while(1):
    stack = []
    tmp=[]
    tmp = input()
    # print(tmp)

    if tmp[0]=='.':
        break

    for i in tmp:
        if i == "(" or i == "[" :
            stack.append(i)
        if i == ")" :
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        if i == "]" :
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

    print("no" if stack else "yes")
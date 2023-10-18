h,m = map(int, input().split())

if(m-45 < 0):
    if(h == 0):
        h = 23
    else:
        h -= 1
    
    m = 60+(m-45)
        
    print(str(h)+" "+str(m))
else:
    print(str(h)+" "+str(m-45))
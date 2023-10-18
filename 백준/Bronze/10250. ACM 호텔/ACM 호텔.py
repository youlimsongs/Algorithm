t = int(input())

for i in range(t):
    H,W,N = map(int, input().split())
    col = N // H 
    row = N % H 

    if(row ==0):
        row = H
        col -= 1

    ho = col + 1

    if( ho < 10):
        print(str(row)+"0"+str(ho))
    else:
        print(str(row)+str(ho))
import sys
input = sys.stdin.readline

number = [[] for _ in range(4)] #pkht
check = [ 0,0,0,0]

tmp = input().strip()
st=[]
for t in tmp:
    st.append(t)


for i in range(len(st)//3):
    if st[i*3] == "P":
        num = st[i*3 + 1] + st[i*3 + 2] # 숫자 추출
        if check[0] == 0 or number[0].count(num) == 0: #처음 나온 수 이ㅣ거나 없으면
            check[0] += 1
            number[0].append(num)
        else:
            print("GRESKA")
            exit()
    if st[i*3] == "K":
        num = st[i*3 + 1] + st[i*3 + 2] # 숫자 추출
        if check[1] == 0 or number[1].count(num) == 0: #처음 나온 수 이ㅣ거나 없으면
            number[1].append(num)
            check[1] += 1
        else:
            print("GRESKA")
            exit()
    if st[i*3] == "H":
        num = st[i*3 + 1] + st[i*3 + 2] # 숫자 추출
        if check[2] == 0 or number[2].count(num) == 0: #처음 나온 수 이ㅣ거나 없으면
            number[2].append(num)
            check[2] += 1
        else:
            print("GRESKA")
            exit()
    if st[i*3] == "T":
        num = st[i*3 + 1] + st[i*3 + 2] # 숫자 추출
        if check[3] == 0 or number[3].count(num) == 0: #처음 나온 수 이ㅣ거나 없으면
            number[3].append(num)
            check[3] += 1
        else:
            print("GRESKA")
            exit()

for i in check: 
    print(13 - int(i), end=' ')
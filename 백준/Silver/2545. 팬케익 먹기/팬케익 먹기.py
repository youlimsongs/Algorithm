t = int(input())
for i in range(t):
    input()
    a,b,c,d = map(int, input().split())

    a, b, c = sorted((a, b, c))

    #남은 길이의 합
    s = a + b + c - d

    tmp = min(s // 3, a) #남은 길이를 abc가 최대한 동일하게 가져가도록, 하지만 평균 길이보다 a가 더 작을 수 있음
    a = tmp #a 길이 설정
    s -= tmp #남은 b,c길이 합
    b = min(s // 2, b) #b,c길이 되도록 동일하게 b길이 설정
    print(a*b*(s-b))
t = int(input())
score = 0
total = 0

for i in range(t):
    res = input()
    total =0
    score =0

    for j in res:
        # print(j)
        if(j == "O"):
            score += 1
            # print(score)
            total += score
            
        else:
            score = 0

    print(total)

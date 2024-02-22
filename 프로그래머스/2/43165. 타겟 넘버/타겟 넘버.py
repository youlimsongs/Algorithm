def solution(numbers, target):
    minus=[]
    for n in numbers:
        minus.append(-n)
    
    global cnt
    cnt=0
    dfs(numbers, target, minus, 0, 0)
    
    return cnt

def dfs(numbers, target, minus, value, dep):
        global cnt
        
        if dep == len(numbers):
            if value == target:
                # print("good")
                cnt += 1
                return
            else:
                # print("no")
                return

        dfs(numbers, target, minus, value + numbers[dep], dep+1)
        dfs(numbers, target, minus, value + minus[dep], dep+1)




    
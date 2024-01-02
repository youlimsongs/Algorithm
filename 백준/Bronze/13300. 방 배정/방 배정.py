import sys
sys_input = sys.stdin.readline

n, k = map(int, sys_input().rstrip().split(" "))
# n, k = sys_input().split()

student=[]
for i in range(6):
    student.append([0,0])
# print(student)

room=12

for i in range(n):
    sex, grade = map(int, sys_input().split())
    if(sex==0):
        student[grade-1][0] += 1
        if(student[grade-1][0] > k):
            room +=1
        
    elif(sex==1):
        student[grade-1][1] += 1
        if(student[grade-1][1] > k):
            room +=1
    

# zero = student[].count(0)
# print(zero)

for i in range(6):
    if(student[i].count(0)>0):
        room -= student[i].count(0)
# room -= zero

print(room)
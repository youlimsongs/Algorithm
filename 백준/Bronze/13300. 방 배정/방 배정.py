import sys
sys_input = sys.stdin.readline

n, k = map(int, sys_input().rstrip().split(" "))
# n, k = sys_input().split()

student=[]
for i in range(6):
    student.append([0,0])
# print(student)

room=0

for i in range(n):
    sex, grade = map(int, sys_input().split())
    student[grade-1][sex] += 1

for i in range(6):
    for j in range(2):
        if(student[i][j]%k == 0):
            room += student[i][j]/k
        else:
            room += student[i][j]//k + 1

print(int(room))
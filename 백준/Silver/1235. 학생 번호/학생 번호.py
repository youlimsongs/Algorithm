import sys
sys_input=sys.stdin.readline

n = int(sys_input())

student=[]

for i in range(n):
    student.append(sys.stdin.readline().strip())


for i in range(1, len(student[0])+1):
    sliced_num = [val[-i:] for val in student]

    if(len(set(sliced_num))==len(student)):
        print(i)
        break
N = int(input())
classes = []
for _ in range(N):
    row = list(map(int, input().split()))
    classes.append(set(row[1:]))

M = int(input())
students = []
for _ in range(M):
    row = list(map(int, input().split()))
    students.append(set(row[1:]))

for student in students:
    cnt = 0
    for c in classes:
        if c.intersection(student) == c: #공통된 원소가 c인경우
            cnt += 1
    print(cnt)
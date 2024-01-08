import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())
daily_study=[]
baek_study = []

for i in range(n):
    log = (sys_input().strip())
    if log.startswith("boj.kr/"):
        baek_study.append(log)
    else:
        daily_study.append(log)

daily_sort = sorted(daily_study, key = lambda k : (len(k), k))
baek_study = sorted(baek_study, key = lambda k : int(k.split("/")[1]))

for res in daily_sort: print(res)
for res in baek_study: print(res)
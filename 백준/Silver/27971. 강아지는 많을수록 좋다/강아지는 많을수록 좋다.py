import sys
input = sys.stdin.readline
N, M, A, B = map(int, input().split(" "))

if A > B:
    A, B = B, A

dp = [0] * (N + 1)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    for j in range(s, e + 1):
        dp[j] = -1

for i in range(1, N + 1):
    if dp[i] == -1:
        continue
    if i < A:
        dp[i] = -1
    elif i < B:
        if dp[i - A] == -1:
            dp[i] = -1
        else:
            dp[i] = dp[i - A] + 1
    elif dp[i - A] == -1 and dp[i - B] == -1:
        dp[i] = -1
    elif dp[i - A] == -1:
        dp[i] = dp[i - B] + 1
    elif dp[i - B] == -1:
        dp[i] = dp[i - A] + 1
    else:
        dp[i] = min(dp[i - A], dp[i - B]) + 1

print(dp[N])
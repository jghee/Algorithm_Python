from sys import maxsize
x = int(input())

dp = [0] * (x + 1)

for i in range(2, x+1):
    a = maxsize
    b = maxsize
    c = maxsize
    d = dp[i-1] + 1

    if i % 5 == 0:
        a = dp[i//5] + 1
    if i % 3 == 0:
        b = dp[i//3] + 1
    if i % 2 == 0:
        c = dp[i//2] + 1

    dp[i] = min(a, b, c, d)

print(dp[x])

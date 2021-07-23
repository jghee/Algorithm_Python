n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(0, n):
    for j in range(i+2, n):
        dp[i] = max(dp[i], a[i] + a[j])
        dp[j] = dp[i]

print(dp)
print(max(dp))

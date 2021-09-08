n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(0, n):
    for j in range(i+2, n):
        dp[i] = max(dp[i], a[i] + a[j])
        dp[j] = dp[i]

# print(dp)
# print(max(dp))
#
#
# n = int(input())
# array = list(map(int, input().split()))
#
# d = [0] * 100
#
# d[0] = array[0]
# d[1] = max(array[0], array[1])
# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + array[i])
#
# print(d[n-1])

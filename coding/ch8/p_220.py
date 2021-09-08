n = int(input())
a = list(map(int, input().split()))
# 두번째 풀이
dp1 = [0] * n
dp2 = [0] * n
dp1[0], dp1[1] = a[0], a[1]
dp2[0], dp2[1] = a[0], a[1]

for i in range(2, n):
    dp1[i] = dp1[i-2] + a[i]
    dp2[i] = max(dp1[i], dp2[i-1])

print(dp2[n-1])

# 최초 풀이
# dp = [0] * n
#
# for i in range(0, n):
#     for j in range(i+2, n):
#         dp[i] = max(dp[i], a[i] + a[j])
#         dp[j] = dp[i]
# print(dp)
# print(max(dp))
#


# 교재 답안 예시
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

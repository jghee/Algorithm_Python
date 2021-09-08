n, m = map(int, input().split())
d = []

for i in range(n):
    d.append(int(input()))

dm = [10001] * (m + 1)
dm[0] = 0

for j in d:
    for i in range(1, m+1):
        if i >= j and dm[i-j] != 10001:
            dm[i] = min(dm[i], dm[i-j] + 1)

# 교재 답안 예시
# for i in range(n):
#     for j in range(d[i], m + 1):
#         if dm[j - d[i]] != 10001:
#             dm[j] = min(dm[j], dm[j - d[i]] + 1)

if dm[m] == 10001:
    print(-1)
else:
    print(dm[m])

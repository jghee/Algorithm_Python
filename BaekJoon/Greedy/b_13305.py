n = int(input())
p = list(map(int, input().split(' ')))
o = list(map(int, input().split(' ')))

minO = o[0]
result = p[0] * minO

for i in range(1, n-1):
    if minO > o[i]:
        minO = o[i]
    result += minO * p[i]

print(result)

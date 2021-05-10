s = list(input().split('-'))
a = list()

for i in s:
    a.append(sum(list(map(int, i.split('+')))))

result = a[0]

for i in range(1, len(a)):
    result -= a[i]

print(result)

n, k = map(int, input().split(' '))
a = []
for i in range(n):
    a.append(int(input()))

r = k
result = 0
a.reverse()

for i in a:
    if r >= i:
        result += r // i
        r = r % i
        if r == 0:
            break
print(result)
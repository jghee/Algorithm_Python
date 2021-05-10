n = int(input())
p = list()

p = list(map(int, input().split(' ')))

p.sort()

pi = list()
pi.append(p[0])

for i in range(1, n):
    pi.append(pi[i-1] + p[i])

print(sum(pi))

from collections import deque

n, m, v = map(int, input().split())

array = [[] for _ in range(n + 1)]
visit1 = [0] * (n + 1)
visit2 = [0] * (n + 1)
result_dfs = []
result_bfs = []

for i in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)

for i in range(1, n + 1):
    array[i].sort()


def dfs(a, start):
    visit1[start] = 1
    result_dfs.append(start)
    for i in a[start]:
        if visit1[i] == 0:
            dfs(a, i)


def bfs(a, start):
    queue = deque()
    queue.append(start)
    visit2[start] = 1

    while queue:
        s = queue.popleft()
        result_bfs.append(s)
        for i in a[s]:
            if visit2[i] == 0:
                queue.append(i)
                visit2[i] = 1


dfs(array, v)
bfs(array, v)

for i in result_dfs:
    print(i, end=' ')
print()
for i in result_bfs:
    print(i, end=' ')

n, m = map(int, input().split())

g = []

for i in range(n):
    g.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if g[x][y] == 0:
        g[x][y] = 1
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False


result = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            result += 1

print(result)
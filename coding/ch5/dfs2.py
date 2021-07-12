from sys import maxsize

n, m = map(int, input().split())

miro = []

for i in range(n):
    miro.append(list(map(int, input())))


def dfs2(x, y, r):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return maxsize
    if miro[x][y] == 1:
        print(x, y)
        miro[x][y] = 0
        r += 1
        if x == n - 1 and y == m - 1:
            return r
        a = dfs2(x + 1, y, r)
        b = dfs2(x - 1, y, r)
        c = dfs2(x, y + 1, r)
        d = dfs2(x, y - 1, r)
        return min(a, b, c, d)
    return maxsize


result = 0
print(dfs2(0, 0, result))


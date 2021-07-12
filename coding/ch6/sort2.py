n = int(input())

info = []

for i in range(n):
    name, score = input().split()
    info.append((name, int(score)))


def setting(data):
    return data[1]


result = sorted(info, key=setting)
# result = sorted(info, key=lambda student: studnet[1])

for i in result:
    print(i[0], end=' ')


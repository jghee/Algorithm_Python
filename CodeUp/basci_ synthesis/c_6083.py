r, g, b = input().split(' ')
result = 0
for i in range(int(r)):
    for j in range(int(g)):
        for k in range(int(b)):
            print(i,j,k)
            result+=1
print(result)
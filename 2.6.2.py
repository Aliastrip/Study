
n = int(input())
answer = 0
flag = 0

for i in range(n):
    i += 1
    for j in range(i):
        print(i, end=' ')
        flag += 1
        if flag >= n:
            break
    if flag >= n:
        break


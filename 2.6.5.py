n = int(input())
x, y = 0, n - 1
lx, ly = 0, 0
spir = [[0] * n for i in range(n)]
flag = n
dl = n - 1


def pr(data: list):
    for i in data:
        print(i)
    print()


for i in range(n):
    spir[0][i] = i + 1

while True:
    for r in range(dl):
        x += 1
        flag += 1
        spir[x][y] = flag
        pr(spir)
    for c in range(dl):
        y -= 1
        flag += 1
        spir[x][y] = flag
        pr(spir)
    dl -= 1
    for r in range(dl):
        x -= 1
        flag += 1
        spir[x][y] = flag
        pr(spir)
    for c in range(dl):
        y += 1
        flag += 1
        spir[x][y] = flag
        pr(spir)
    if flag == n*n:
        break
    dl -= 1


        # 00 01 02 03 04
        # 10 11 12 13 14
        # 20 21 22 23 24
        # 30 31 32 33 34
        # 40 41 42 43 44

print(spir)
seriesOfNumber = [int(i) for i in input().split()]
x = int(input())
flag = 0

if x not in seriesOfNumber:
    print("Отсутствует")
else:
    for j in seriesOfNumber:
        if j == x:
            print(flag, end=' ')
        flag += 1


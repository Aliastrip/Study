
a = int(input())
b = int(input())
answer = 0
summ = 0
flag = 0

for i in range(a, b+1):
    if i % 3 == 0:
        summ += i
        # print(i, summ)
        flag += 1

answer = summ / flag

print(answer)

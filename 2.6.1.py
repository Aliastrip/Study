s = int(input())
answer = s ** 2
while s != 0:
    number = int(input())
    s += number
    answer += number ** 2

print(answer)

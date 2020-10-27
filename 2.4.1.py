
gc = input()

answer = 0
flag = 0

for i in gc.lower():
    if i == 'g' or i == 'c':
        flag += 1

answer = (flag / len(gc)) * 100

print(answer)

a = int(input())
b = int(input())

d = 1

if a == b:
    d = a
else:
    while (d % a) != 0 or (d % b) != 0:
        d += 1

print(d)


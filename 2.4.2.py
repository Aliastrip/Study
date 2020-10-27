gen = input()
codegen = ""
k = 0
flag = 1

for i in range(len(gen) - 1):
    if gen[i] == gen[i + 1]:
        flag += 1
    else:
        codegen += (gen[i] + str(flag))
        flag = 1
    i += 1
    k = i

codegen += (gen[k] + str(flag))
print(codegen)

k = 0
matrix = []
data = []

while True:
    current = input()
    if current == 'end':
        break
    matrix.append(list(int(i) for i in current.split(' ')))

rows = len(matrix)
cols = len(matrix[0])
a = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        if i + 1 < rows and j + 1 < cols:
            a[i][j] = matrix[i][j - 1] + matrix[i][j + 1] + matrix[i - 1][j] + matrix[i + 1][j]
        elif i + 1 >= rows and j + 1 < cols:
            a[i][j] = matrix[i][j - 1] + matrix[i][j + 1] + matrix[i - 1][j] + matrix[0][j]
        elif i + 1 < rows and j + 1 >= cols:
            a[i][j] = matrix[i][j - 1] + matrix[i][0] + matrix[i - 1][j] + matrix[i + 1][j]
        else:
            a[i][j] = matrix[i][j - 1] + matrix[i][0] + matrix[i - 1][j] + matrix[0][j]

for r in a:
    for c in r:
        print(c, end=' ')
    print()


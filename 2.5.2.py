data = [int(i) for i in input().split(' ')]


def run():
    global data
    n = len(data)
    if n == 1:
        print(data[0])
        return

    indexes = [(i - 1, i + 1) for i in range(n)]

    print(indexes)
    indexes[n - 1] = indexes[n - 1][0], 0
    print(indexes)

    for i, j in indexes:
        print(data[i] + data[j], end=' ')


run()

from math import ceil as cl, floor as fl


def solve():
    a, b = map(int, input().split())

    return (cl(a / 2) * cl(b / 2)) + (fl(a / 2) * fl(b / 2))


for i in range(int(input())):
    print(solve())
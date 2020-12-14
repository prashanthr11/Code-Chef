from math import ceil as cl


def solve():
    a, b = map(int, input().split())
    l = list(map(int, input().split()))
    risk, nonrisk = 0, 0

    for i in l:
        if i <= 9 or i >= 80:
            risk += 1
        else:
            nonrisk += 1

    return cl(risk / b) + cl(nonrisk / b)


for i in range(int(input())):
    print(solve())
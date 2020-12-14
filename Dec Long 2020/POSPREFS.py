def solve():
    a, b = map(int, input().split())
    l = [-(i + 1) for i in range(a)]

    if a == b:
        return [abs(i) for i in l]

    i, j = 0, 1
    while i < b and j < a:
        l[j] = -l[j]
        j += 2
        i += 1

    j = a - 1 if a % 2 else a - 2
    while i < b and j > -1:
        l[j] = -l[j]
        j -= 2
        i += 1

    return l


for i in range(int(input())):
    print(*solve())
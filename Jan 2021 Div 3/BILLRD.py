def solve_at_1(x, y, n):
    mini = min(n - x, n - y)
    return (x + mini, y + mini)

    while x < n and y < n:
        x += 1
        y += 1

    return (x, y)


def solve_at_0(x, y, n):

    mini = min(x, y)
    return (x - mini, y - mini)

    while x > 0 and y > 0:
        x -= 1
        y -= 1

    return (x, y)


def solve():
    a, b, c, d = map(int, input().split())

    if c == d:
        return (a, a)

    l = list()

    l.append(solve_at_0(c, d, a))
    x1, y1 = solve_at_1(c, d, a)
    l.append((x1, y1))
    l.append((y1, x1))

    l.append(solve_at_0(y1, x1, a))

    # print(l)
    return l[b % 4]


for i in range(int(input())):
    a, b = solve()
    print(a, b)
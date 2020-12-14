from math import ceil as cl


def solve1(ans, target, day, v):
    i = ans + 1

    while i < day and target > 0:
        ans += 1
        target -= v
        i += 1

    return target, ans


def solve():
    d1, v1, d2, v2, target = map(int, input().split())

    if d1 == d2:
        return cl(target / (v1 + v2)) + d1 - 1

    vaccines_per_day = v1 + v2

    if d1 < d2:
        tmp = solve1(d1 - 1, target, d2, v1)
        if tmp[0] > 0:
            return tmp[1] + cl(tmp[0] / vaccines_per_day)
        return tmp[1]
    else:
        tmp = solve1(d2 - 1, target, d1, v2)
        if tmp[0] > 0:
            return tmp[1] + cl(tmp[0] / vaccines_per_day)
        return tmp[1]


if __name__ == "__main__":
    print(solve())
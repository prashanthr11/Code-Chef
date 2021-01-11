from heapq import heapify, heappop, heappush


def solve():
    t1, t2 = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0

    a_sum, b_sum = sum(a), sum(b)

    if a_sum > b_sum:
        return cnt

    if t1 == t2 and a_sum == b_sum:
        return -1

    heapify(a)
    b = [-i for i in b]
    heapify(b)

    while a_sum <= b_sum:

        x, y = heappop(a), -heappop(b)
        # print(x, y)

        if x >= y:
            return -1

        diff = y - x
        a_sum, b_sum = a_sum + diff, b_sum - diff
        heappush(a, y)
        heappush(b, x)
        cnt += 1

    return cnt


for i in range(int(input())):
    print(solve())
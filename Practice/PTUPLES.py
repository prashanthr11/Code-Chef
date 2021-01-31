def seive(b):
    b += 1
    pr = [True] * b
    ret = []
    pr[0] = pr[1] = False
    
    for i in range(2, b):
        if pr[i]:
            for j in range(i * i, b, i):
                pr[j] = False
                
            if pr[i - 2]:
                ret.append(i)

    return ret


from bisect import bisect_left


def solve():
    x = int(input())
    return bisect_left(pr, x + 1)


pr = seive(10**6)
for i in range(int(input())):
    print(solve())


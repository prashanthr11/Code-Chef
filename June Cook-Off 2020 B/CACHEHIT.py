def check(l, b, m):
    l2 = list()
    cache_now = [[]]
    for i in range(0, len(l), b):
        l2.append(l[i:i + b])
    cnt = 0
    qr = list(map(int, input().split()))
    for i in qr:
        if i not in cache_now[0]:
            cnt += 1
            cache_now.clear()
            for x in range(len(l2)):
                if i in l2[x]:
                    cache_now.append(l2[x])
                    break
    return cnt
              

for i in range(int(input())):
    n, b, m = map(int, input().split())
    l = [i for i in range(n)]
    print(check(l, b, m))

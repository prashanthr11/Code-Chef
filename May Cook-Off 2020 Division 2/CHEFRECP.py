def check(l):
    d = defaultdict(lambda: 0)
    for i in range(len(l)):
        if d[l[i]]:
            if l[i - 1] == l[i]:
                d[l[i]] += 1
            else:
                return 'NO'
        else:
            d[l[i]] += 1
    if len(set(d.keys())) == len(set(d.values())):
        return 'YES'
    else:
        return 'NO'



from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(check(l))

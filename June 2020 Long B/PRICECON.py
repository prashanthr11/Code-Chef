for i in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    temp = list()
    loss = 0
    total = sum(l)
    for i in l:
        if i > k:
            temp.append(k)
        else:
            temp.append(i)
    print(total - sum(temp))

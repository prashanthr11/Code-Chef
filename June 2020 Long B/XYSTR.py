for i in range(int(input())):
    s = input()
    cnt = 0
    l = list()
    for i in range(len(s)):
        if len(l):
            if l[-1] == "x" and s[i] == "y" or s[i] == "x" and l[-1] == "y":
                l.pop()
                cnt += 1
        else:
            l.append(s[i])
    print(cnt)

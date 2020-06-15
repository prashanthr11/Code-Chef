t = int(input())
for i in range(t):
    n = int(input())
    f = 0
    t = 0
    flag = True
    icrm = list(map(int,input().split()))
    for j in range(len(icrm)):
        if icrm[j]==5:
            f += 1
        elif icrm[j]==10:
            if f > 0:
                f -= 1
                t += 1
            else:
                flag = False
                break
        else:
            if icrm[j]==15:
                if t > 0:
                    t -= 1
                elif f >= 2:
                    f -= 2
                else:
                    flag = False
                    break
    if flag:
        print('YES')
    else:
        print('NO')

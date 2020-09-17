from calendar import isleap

def solve(l):
    y, m, d = map(int, l)
    
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if isleap(y):
        l[1] = 29
    
    # print(l)
    
    if l[m - 1] % 2 == 0:
        if d % 2:
            return 16 + 1 + (l[m - 1] - d) // 2
        else:
            return 16 + (l[m - 1] - d) // 2
    
    return 1 + (l[m - 1] - d) // 2
    

for i in range(int(input())):
    print(solve(input().split(':')))
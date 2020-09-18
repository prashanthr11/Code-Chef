    
def solve(a, b):
    if a <= b:
        return 1
        
    while a > b:
        if b == 0:
            return 0
        a -= b
        b //= 2
    
    if a <= b:
        return 1
    return 0
    
    
for i in range(int(input())):
    n, m = map(int, input().split())
    print(solve(n, m))
    

def solve():
    n = int(input())
    n = 120 - n
    
    s = input().count('1')
    
    res = ((n + s) / 120) * 100
    
    return 'YES' if res >= 75 else 'NO'
    

for i in range(int(input())):
    print(solve())

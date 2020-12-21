def solve():
    s = input()
    
    x, y = s.count('0'), s.count('1')
    
    if len(s) % 2 or x == len(s) or len(s) == y:
        return -1
    
    return (len(s) // 2) - y if x > y else (len(s) // 2) - x

for i in range(int(input())):
    print(solve())

def solve():
    a, b = map(int, input().split())
    
    return (2 * b) - (2 * a) + 1


for i in range(int(input())):
    print(solve())

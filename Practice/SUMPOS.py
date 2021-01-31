def solve():
    a, b, c = map(int, input().split())
    if a + b == c or a + c == b or b + c == a:
        return 'YES'
    return 'NO'


for i in range(int(input())):
    print(solve())

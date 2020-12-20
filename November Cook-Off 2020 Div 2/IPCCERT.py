def solve(l, q, b):
    if sum(l) >= b and q <= 10:
        return True
    return False


a, b, c = map(int, input().split())
cnt = 0
for i in range(a):
    l = list(map(int, input().split()))
    if solve(l[:-1], l[-1], b):
        cnt += 1

print(cnt)

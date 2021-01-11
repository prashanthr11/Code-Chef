def solve():
    setters, required_problems, days = map(int, input().split())
    problems = list(map(int, input().split()))
    total_problems = sum(problems)

    return min(total_problems // required_problems, days)


for i in range(int(input())):
    print(solve())
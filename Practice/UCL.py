from collections import defaultdict as di


def solve():
    point = di(int)
    goal_diff = di(int)
    
    for i in range(12):
        a, b, c, e, d = input().split()
  
        goal_diff[a] = goal_diff[a] + int(b) - int(e)
        goal_diff[d] = goal_diff[d] + int(e) - int(b)
        
        if int(b) > int(e):
            point[a] += 3
        elif int(b) < int(e):
            point[d] += 3
        else:
            point[a] += 1
            point[d] += 1
        
    ans = {}
    
    for i in point:
        ans[i] = (point[i], goal_diff[i])
    
    cnt = 0
    
    for k, v in sorted(ans.items(), key = lambda x:x[1], reverse = True):
        if cnt < 2:
            print(k, end = ' ')
        else:
            break
        cnt += 1
        
    print()

for i in range(int(input())):
    solve()
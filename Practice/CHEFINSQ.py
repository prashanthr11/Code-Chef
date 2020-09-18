from itertools import combinations as comb
from collections import defaultdict as di
import time

def solve(m):
    l = list(map(int, input().split()))
    ans = list(comb(l, m))
        
    ans.sort()
    d = di(int)
    
    for i in ans:
        d[sum(i)] += 1
    
    if len(d):
        mini = min(d.keys())
    
    return d[mini]

for i in range(int(input())):
    n, m = map(int, input().split())
    print(solve(m))

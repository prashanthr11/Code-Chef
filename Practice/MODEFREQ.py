from collections import Counter as di


def solve(l):
    freq = di(l)
    mode_freq = di(freq.values())
    
    maxi = max(mode_freq.values())
    
    ans = set()
    for i in mode_freq:
        if mode_freq[i] == maxi:
            ans.add(i)
            
    mini = int(1e9)
    
    for i in freq:
        if freq[i] in ans:
            mini = min(mini, freq[i])
    
    return mini
    

for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    print(solve(l))
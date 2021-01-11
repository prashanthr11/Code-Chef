def solve(string, letters):
    # Method 1 (Straight Forward)
    ret = ''
    for i in range(0, len(string), 4):
        ln, alphabets = 16, letters

        for j in string[i:i + 5]:

            ln //= 2

            if j == '1':
                alphabets = alphabets[ln:]
            else:
                alphabets = alphabets[:ln]

        ret += alphabets[0]

    return ret


for i in range(int(input())):
    length = int(input())
    string = input()
    letters = [chr(i) for i in range(97, 97 + 16)]
    print(solve(string, letters))

'''
# Method 2 (Recursion)

def solve(string, letters, ret):
    
    if not string:
        return ret
        
    alphabets = letters
    ln = 16
    for j in string[:i + 5]:
        
        ln //= 2
        
        if j == '1':
            letters = letters[ln:]
        else:
            letters = letters[:ln]
        
    ret += letters[0]
    return solve(string[4:], alphabets, ret)


letters = [chr(i) for i in range(97, 97 + 16)]
for i in range(int(input())):
    length = int(input())
    string = input()
    print(solve(string, letters, ''))
'''
def recursion(s, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

# print('ABBA: ', isPalindrome('ABBA'))
# print('ABC: ', isPalindrome('ABC'))

N = int(input())
for _ in range(N):
    testcase = input()
    cnt = 0
    print(*isPalindrome(testcase))

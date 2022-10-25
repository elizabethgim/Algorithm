import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
newArr = []
for a in arr:
    newArr.append(a/max(arr)*100)
# print(newArr)
print(sum(newArr)/N)
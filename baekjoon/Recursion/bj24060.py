import sys

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr)+1) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    temp = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left):
        temp.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        temp.append(right[j])
        ans.append(right[j])
        j += 1

    return temp


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = []
merge_sort(arr)

if len(ans) >= K:
    print(ans[K-1])
else:
    print(-1)

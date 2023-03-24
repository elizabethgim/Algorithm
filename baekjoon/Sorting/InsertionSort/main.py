# import sys
# arr = list(map(int, sys.stdin.readline().split()))
arr= [40, 60, 70, 50, 10, 20, 30]
sorted_arr = []
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]

print(arr)
'''
skeleton code
for i: 1 to length(A)-1
j = i
while j > 0 and A[i-1] > A[i]
    swqp A[j] and A[j-1]
    j = j-1

기존에 있던 값들은 이전 패스에서 모두 정렬되었다는 점을 활용하면 불필요한 비교 작업을 제거
'''

def insertion_sort(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1

    return arr

if __name__ == "__main__":
    print(insertion_sort([40, 60, 70, 50, 10, 20, 30]))
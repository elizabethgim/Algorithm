'''
1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
3. 판매는 얼마든지 할 수 있다.

'''

T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_p = 0

    profit = 0
    for i in range(N-1, -1, -1):
        if max_p < arr[i]:
            max_p = arr[i]

        profit += max_p - arr[i]

    print("#{} {}".format(t+1, profit))

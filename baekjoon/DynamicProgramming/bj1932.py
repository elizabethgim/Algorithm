import sys

N = int(sys.stdin.readline())
dp = []

for _ in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))

# bottom-up
for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            dp[i][0] += dp[i-1][0]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1]))

# top-down 시도
# for i in range(N-2):
#     temp = []
#     for j in range(2**i):
#         temp.append(dp[i][j] + arr[i + 1][j])
#         temp.append(dp[i][j] + arr[i + 1][j + 1])
#     dp.append(temp)
# print(dp)

'''
[7]

[3, 8]
dp[0][0] + dp[i+1][0], dp[i][0] + dp[i+1][1]

[8, 1, 0]
dp[1][0] + dp[2][0], dp[1][0] + dp[2][1],
dp[1][1] + dp[2][1], dp[1][1] + dp[2][2],

'''
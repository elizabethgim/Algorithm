chess = [1, 1, 2, 2, 2, 8]
count = list(map(int, input().split()))
result = []
for i in range(len(chess)):
    result.append(chess[i] - count[i])
print(*result, sep=" ")
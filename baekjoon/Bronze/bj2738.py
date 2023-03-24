import sys
N, M = map(int, sys.stdin.readline().split())
matrix1 = []
for _ in range(N):
    matrix1.append(list(map(int, sys.stdin.readline().split())))

matrix2 = []
for _ in range(N):
    matrix2.append(list(map(int, sys.stdin.readline().split())))

total = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        total[i][j] = matrix1[i][j] + matrix2[i][j]

for i in range(N):
    print(*total[i], sep=' ')


import sys
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
total = 0
for _ in range(N):
    p, n = map(int, sys.stdin.readline().strip().split())
    total += p*N

if X == total:
    print("Yes")
else:
    print("No")
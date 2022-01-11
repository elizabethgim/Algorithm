import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
num3 = int(sys.stdin.readline())

total = num1 * num2 * num3
numbers = str(total)

res = {}

for i in range(10):
    n = str(i)
    res[i] = 0
    for j in range(len(numbers)):
        if n == numbers[j]:
            res[i] += 1

for v in res.values():
    print(v)

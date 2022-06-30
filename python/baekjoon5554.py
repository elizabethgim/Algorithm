import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
num3 = int(sys.stdin.readline())
num4 = int(sys.stdin.readline())

sum = num1 + num2 + num3 + num4
min = sum // 60
sec = sum - min * 60

print(min)
print(sec)
import sys

T = int(sys.stdin.readline())

def fibonacci(n):
    global zero, one
    if n == 0:
        zero += 1
        return 0

    elif n == 1:
        one += 1
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibo_zero = [0] * 41
fibo_one = [0] * 41

for _ in range(T):
    N = int(sys.stdin.readline())
    # fibo = [0, 1]
    # zero, one = 0, 0
    # fibonacci(N)
    # print(zero, one)
    fibo_zero[0] = 1
    fibo_one[1] = 1

    if N > 1:
        for i in range(2, N+1):
            fibo_zero[i] = fibo_zero[i-2] + fibo_zero[i-1]
            fibo_one[i] = fibo_one[i-2] + fibo_one[i - 1]

    print(fibo_zero[N], fibo_one[N])

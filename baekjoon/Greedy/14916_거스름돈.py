# 참고: https://velog.io/@tunaman95/%EB%B0%B1%EC%A4%80-14916%EB%B2%88-%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88-Python
n = int(input())
cnt = 0

while n > 0:
    print(n)
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1

if n < 0:
    print(-1)
else:
    print(cnt)
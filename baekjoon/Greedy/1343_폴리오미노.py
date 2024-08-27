
line = input()
N = len(line)
tmp = ['' for _ in range(N+1)]
aa = 4
bb = 2

cnt = 0
answer = ""
for i in range(1, N+1):
    if line[i-1] == "X":
        cnt += 1

    if cnt % 4 == 0:
        tmp[i] = "AAAA"
    elif cnt % 2 == 0:
        tmp[i] = "BB"

print(tmp)
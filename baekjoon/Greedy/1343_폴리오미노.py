line = input()

# line = line.replace("XXXX", "AAAA")
# line = line.replace("XX", "BB")
#
# if 'X' in line:
#     print(-1)
# else:
#     print(line)
# 출처: https://s0ng.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8F%B4%EB%A6%AC%EC%98%A4%EB%AF%B8%EB%85%B8-1343%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
# 파이썬 사기야..

# 출처: https://ddiyeon.tistory.com/15
cnt = 0
i = 0
answer = ""

while i < len(line):
    if line[i: i+4] == "XXXX":
        answer += "AAAA"
        i += 4
    elif line[i: i+2] == "XX":
        answer += "BB"
        i += 2
    elif line[i] == 'X':
        answer = -1
        break
    else:
        answer += line[i]
        i += 1

print(answer)
'''
N = len(line)
tmp = ['' for _ in range(N+1)]
aa = 4
bb = 2

cnt = 0
answer = ""
for i in range(N):
    if line[i] == "X":
        cnt += 1

    if line[i] == ".":
        answer += "."
        if cnt % 2 != 0:
            break
        else:
            cnt = 0

    if cnt % 4 == 0:
        tmp[i] = "AAAA"
        cnt = 0
        answer += "AAAA"
    elif cnt % 2 == 0:
        tmp[i] = "BB"
        answer += "BB"

print(tmp)
print(answer)
'''
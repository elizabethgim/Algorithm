import sys

line = sys.stdin.readline()
minus = line.split('-')
answer = 0

plus = sum(map(int, (minus[0].split('+'))))

if line[0] == '-':
    answer -= plus
else:
    answer += plus

for x in minus[1:]:
    total = sum(map(int, (x.split('+'))))
    answer -= total

print(answer)
'''
코드 출처: https://puleugo.tistory.com/29

'''
# arr = []
# nums = []
# total = 0
# op = ''
#
# for word in line:
#     if word == '+' or word == '-' or word == '\n':
#         newNum = ''
#         for n in nums:
#             newNum += n
#         nums = []
#         print(newNum)
#         arr.append(newNum)
#         if op == '+':
#             total += int(newNum)
#         elif op == '-':
#             total -= int(newNum)
#         else:
#            total += int(newNum)
#         op = word
#         arr.append(op)
#
#     else:
#         nums.append(word)
#
# print(arr)
# print(total)

'''
55-50+40
'''
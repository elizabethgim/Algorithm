import sys

N = int(sys.stdin.readline())
dot = []
x_dot = []
y_dot = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dot.append([x, y])

for d in sorted(dot):
    print(d[0], d[1])


# print("Insertion Sorting")
# print(dot)
# for i in range(len(dot)):
#     for j in range(i, 0, -1):
#         if dot[j][0] < dot[j-1][0]:
#             dot[j], dot[j-1] = dot[j-1], dot[j]
#         else:
#             if dot[j][1] < dot[j-1][0]:
#                 dot[j], dot[j - 1] = dot[j - 1], dot[j]
#
# print(dot)

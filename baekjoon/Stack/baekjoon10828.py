testCase = int(input())
# testCase = 1
stack = []

while(testCase):
    task = input()

    testCase -= 1
    check = task.split(" ")

    if len(check) > 1:  # push X : 정수 X를 스택에 넣는 연산
        stack.append(int(check[1]))

    else:
        if task == "pop":
            if len(stack) == 0:
                num = -1
            else:
                num = stack.pop()
            print(num)
        elif task == "size":
            print(len(stack))
        elif task == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif task == "top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])

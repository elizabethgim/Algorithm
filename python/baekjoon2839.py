# testCases = int(input())
# number = int(input())

testCases = 1
number = 11
for i in range(testCases):
    five = None
    three = None

    if (number % 5 % 3) == 0:
        five = (number // 5) + (number % 5 // 3)
        
    if (number % 3) == 0:
        three = number // 3

    print(five, three)
    if three != None and five != None:
        if three < five:
            answer = three
        else:
            answer = five
    else:
        if three != None:
            answer = three
        elif five != None:
            answer = five
        else:
            answer = -1
    
    print(answer)
    

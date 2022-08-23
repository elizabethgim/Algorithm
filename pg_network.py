def solution(n, computers):
    answer = 0
    com = {}
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                if i in com:
                    com[i].append(j)
                else:
                    com[i] = [j]

    
    print(com)
    for key in com:
        print(com[key])
        value = com[key]
        
    
    return answer
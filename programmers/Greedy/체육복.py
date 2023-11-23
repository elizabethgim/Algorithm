def solution(n, lost, reserve):
    answer = 0
    cloths = [1 for _ in range(n)]
    for i in reserve:
        cloths[i - 1] += 1

    for i in lost:
        cloths[i - 1] -= 1

    if cloths[0] == 0 and cloths[1] > 1:
        cloths[0] += 1
        cloths[1] -= 1

    for i in range(1, n - 1):
        if cloths[i] == 0:
            if cloths[i - 1] > 1:
                cloths[i - 1] -= 1
                cloths[i] += 1
            elif cloths[i + 1] > 1:
                cloths[i + 1] -= 1
                cloths[i] += 1

    if cloths[n - 1] == 0 and cloths[n - 2] > 1:
        cloths[n - 1] += 1
        cloths[n - 2] -= 1
    print(cloths)

    for i in range(n):
        if cloths[i] > 0:
            answer += 1

    return answer
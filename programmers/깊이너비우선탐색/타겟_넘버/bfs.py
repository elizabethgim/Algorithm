def solution(numbers, target):
    answer = 0
    stack = [(0, 0)] # idx, total
    
    while stack:
        idx, total = stack.pop()
        if idx == len(numbers):
            if total == target:
                answer += 1
            continue
        
        stack.append((idx+1, total + numbers[idx]))
        stack.append((idx+1, total - numbers[idx]))
        
    return answer
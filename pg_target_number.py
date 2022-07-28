answer = 0  # 타겟 넘버가 되는 경우의 수
depth = 0   # 깊이
total = 0   # 더한 값

def solution(numbers, target):
    
    def dfs(total, number, depth):
        total += number
        depth += 1

        if len(numbers) == depth:
            if target == total:
                answer += 1
            depth = 0
            
        dfs(total, -number, depth)
        dfs(total, -number, depth)
        
    for num in numbers:            
        dfs(total, num, depth)
        dfs(total, -num, depth)
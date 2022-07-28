def solution(numbers, target):
    answer = 0
    
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    
    dfs(0, 0)
    return answer

'''
    입력 데이터가 배열이다.
'''
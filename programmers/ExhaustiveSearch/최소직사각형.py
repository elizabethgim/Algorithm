def solution(sizes):
    answer = 0
    max_r = 0
    max_c = 0

    for row, column in sizes:
        if row > column:
            row, column = column, row

        if max_r < row:
            max_r = row
        if max_c < column:
            max_c = column

    answer = max_r * max_c

    return answer

'''
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

문제 풀이 아이디어:
가로와 세로 중 짧은 길이를 세로로 설정하기

'''
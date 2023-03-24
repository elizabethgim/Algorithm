'''
프로그래머스 고득점 kit
전화번호목록, Lv.2
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42577#
문자 배열을 sort()하면 비슷한 문자로 시작한 원소끼리 정렬된다.
'''
def hash(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False

    return answer

def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            for j in range(len(phone_book[i])):
                if phone_book[i][j] == phone_book[i + 1][j]:
                    answer = False
                    break
            if not answer:
                break

    #     phone_numbers = []
    #     for i in range(len(phone_book)):
    #         dic = {}
    #         for j in range(len(phone_book[i])):
    #             dic[j] = phone_book[i][j]
    #         phone_numbers.append(dic)

    #     for i in range(len(phone_book)):
    #         curr = phone_book[i]
    #         print(curr)
    #         for j in range(i+1, len(phone_book)):
    #             check = phone_book[j]
    #             print(curr, check, len(curr))

    #             for k in range(len(curr)):
    #                 print(phone_numbers[i][k], phone_numbers[j][k])
    #                 if phone_numbers[i][k] == phone_numbers[j][k]:
    #                     answer = False
    #                     break

    #             if not answer:
    #                 break

    #         if not answer:
    #             break

    return answer

if __name__ == "__main__":
    solution(["119", "97674223", "1195524421"]) # false
    solution(["123","456","789"]) # true
    solution(["12","123","1235","567","88"]) # false

    # 내가 생각해낸 반례
    solution(["1", "12", "123"]) # false
    solution(["23", "32"]) # ture


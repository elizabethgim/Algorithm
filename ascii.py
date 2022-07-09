def solution(sentences, n):
    answer = -1
    score = {}
    alphabet = {}
    keyboard = {}

    for sentence in sentences:
        no_blank = sentence.split()

        key = set() # 키보드 개수
        alph = set() # 알파벳 종류
        
        for letter in no_blank:

            if letter.isupper(): # 대문자인 경우
                key = key | set(letter.lower())
            
            alph = alph | set(letter)
            key = key | set(letter)

        print("alph", alph, len(alph)) # 사용한 알파벳 개수
        print("key", key, len(key)) # 사용한 키보드
        
        alphabet[sentence] = len(alph)
        keyboard[sentence] = len(key)
        
        # if key == alph:
        score[sentence] = len(sentence)
    
    print("score", score)
    print("alphabet", alph)
    print("keyboard", key)

    return answer
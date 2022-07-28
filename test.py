# a = 123
# b = 3.14
# c = 'hi'
# print('%d, %f, %s'%(a, b, c))

# a = list(range(1, 6, 2))
# a.append(10)
# a.remove(1)

# for x in a:
#     print(x, end=' ')

# a={'사과', '배', '딸기'}
# a.add('수박')
# a.add('배')

# a.remove('사과')
# a.update({'포도', '딸기', '귤'})
# print(a)


# a={'이름':'유이아', '성별': '여', '직업': '무직'}
# a['국가']='한국'
# del a['성별']
# a['직업'] = '가수'

# print(a)

a = 100
result = 0
for i in range(1,3):
    result = a >> i
    print(result)
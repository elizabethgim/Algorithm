# 거스름돈
# https://velog.io/@jiffydev/%EC%9D%B4%EB%A1%A0%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

n=1260 #받은 돈
cnt=0
lst=[500,100,50,10] # 거스름돈 종류

for i in lst:
  cnt+=n//i
  n%=i

print(cnt)
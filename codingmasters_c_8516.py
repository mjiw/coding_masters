# 문서 통계 내기
# 출력 : 첫번째 줄-공백을 포함한 글자수 / 두번째 줄-공백을 제외한 글자수 / 세번째 줄-단어의 수
text=input()

a_len=len(text)
b=[]
for i in text:
    if i==' ':
        continue
    else:
        b.append(i)
# join은 문자열 반환

b_len=len(b)

c=text.split()
# split은 리스트 반환
c_len=len(c)
print(a_len)
print(b_len)
print(c_len)
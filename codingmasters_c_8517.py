# timeout 문제 해결해야함

a,b=map(int,input().split())
sum_=0
d=[]
d+=[[1]*2]
flag=2
for i in range(1,b):
    if i>=2:
        flag+=d[i-2][1]
    d+=[[flag]*flag]

answer=sum(d,[])

for i in range(a-1,b):
    sum_+=answer[i]
print(sum_)
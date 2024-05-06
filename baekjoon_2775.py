t=int(input())
d=[[] for _ in range(t+1)]

# 0층에 대한 각 호실의 인원 구하기
for i in range(0,15):
    d[0].append(i)

# t에 대해 각 층의 각 호실의 인원 구하기
temp=0
for i in range(t):
    k=int(input())
    n=int(input())
    for a in range(1,k+1):
        if len(d[a]) != 0:
            continue
        if a>1:
            for b in range(0,n):
                temp+=d[a-1][b]
                d[a].append(temp)
            temp=0
        else:       
            for b in range(1,n+1):
                temp+=d[a-1][b]
                d[a].append(temp)
            temp=0
    print(d)
    print(d[k][n-1])


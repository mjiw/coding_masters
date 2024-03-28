# 무향 그래프 : 무향 그래프가 주어졌을 때, 각 정점이 연결되어 있는 상황을 출력하는 프로그램
# 시간 줄일 필요가 있음

# 정점의 개수 n과 간선의 개수 m
n,m=map(int,input().split()) 
result=[[0 for _ in range(n)] for _ in range(n)]
gra=[[map(int,input().split())]for _ in range(m)]

for i in range(m):
    for a,b in gra[i]:
        result[a-1][b-1]=1
        result[b-1][a-1]=1
        
# for i in range(m):
#     a,b=map(int,input().split())
#     result[a-1][b-1]=1
#     result[b-1][a-1]=1
    
for i in range(n):
    for j in range(n):
        print(result[i][j],end=' ')
    print(end='\n')
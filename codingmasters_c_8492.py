# 바닥공사 : 1X1, 2X1 의 타일을 가지고 바닥 채우기
# 가로길이 : n, 세로길이 : 1
def b(n):
    a=[]
    flag=0
    for i in range(0,n+1):
        a.append(i)
        print(a[i])
        if i>=3:
            flag=a[i-2]+a[i-1]
            a.append(flag)
            print('c',a)
    return a[n]
    
n=int(input())
print(b(n)%796796)
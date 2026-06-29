n= int(input())

for i in range(n):
    
    x= int(input())
    a= list(map(int,input().split()))
    m=max(a)
    p=min(a)
    count=(m-p+1)//2
    print(count)

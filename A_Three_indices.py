t=int(input())
for _ in range(t):
    n=int(input())
    arry=list(map(int,input().split()))
    for i in range(1,n-1):
        if arry[i]> arry[i-1] and arry[i]>arry[i+1]:
            print("YES")
            print (i,i+1,i+2)
            break
    else:
        print("NO")
            

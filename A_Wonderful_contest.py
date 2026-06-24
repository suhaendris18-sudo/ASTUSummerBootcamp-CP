p=int(input())
for i in range(p):
    n=int(input())
    a=list(map(int,input().split()))
    if 100 in a:
        print('Yes')
    else:
        print('No')  
        

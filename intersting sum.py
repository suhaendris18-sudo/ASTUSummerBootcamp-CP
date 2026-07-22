for _ in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    
    
    print(((arr[-2]-arr[1])+(arr[-1]-arr[0])))
   

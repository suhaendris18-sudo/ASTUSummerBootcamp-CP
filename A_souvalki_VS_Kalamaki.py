for _ in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    for i in range(1,n-1,2):
            if arr[i]==arr[i+1]:
                print("YES")
                break
                
    else:
        print("NO")

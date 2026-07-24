for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=sorted(set(arr))
    
    temp=[]
    from collections import Counter
    freq=Counter(arr)
    for key, value in freq.items():
        if value >= 2:
            for _ in range(value-1):
                temp.append(key)

    print(*(ans+temp))

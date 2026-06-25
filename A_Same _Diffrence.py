t= int(input())
for i in range(t):
    n= int(input())
    s= input()
    count=0
    last=s[-1]
    for i in range(len(s)-1,-1,-1):
        if last!=s[i]:
            count+=1
    print(count)

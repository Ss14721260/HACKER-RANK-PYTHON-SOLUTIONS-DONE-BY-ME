# Enter your code here. Read input from STDIN. Print output to STDOUT

m,n=map(int,input().split())
l=[]
k=[]
for i in range(m):
    a=input()
    l.append(a)
for j in range(n):
    b=input()
    k.append(b)
for i in range(1,len(k)+1):
    if k[i-1] not in l:
            print(-1)
    else:
        inj=[]
        for j in range(1,len(l)+1):
            if k[i-1] == l[j-1]:
                inj.append(str(j))
        print(' '.join(inj))

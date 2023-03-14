A=list(map(int,input().split()))
n=int(input())
for i in range(0,n):
    s=0
    sub=list(map(int,input().split()))
    for j in sub:
        if ((j not in A) or (len(A)<=len(sub))):
            s=1
            break
    if s==1:
        break
if s==0:
    print("True")
else:
    print("False")

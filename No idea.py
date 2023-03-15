# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
arr=list(input().split())
A=set(input().split())
B=set(input().split())
ca=0
for i in arr:
    if i in A:
        ca+=1
    if i in B:
        ca-=1
print(ca)

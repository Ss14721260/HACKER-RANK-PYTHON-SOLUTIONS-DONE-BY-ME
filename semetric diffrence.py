# Enter your code here. Read input from STDIN. Print output to STDOUT
m=input()
a=set(map(int,input().split()))
n=input()
b=set(map(int,input().split()))
syd=(a.difference(b)).union(b.difference(a))
s=list(syd)

for i in sorted(s):
    print(i)

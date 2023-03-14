# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
y=input().split(" ")
n=int(input())
s=0
for i in range(n):
    yi,xi=map(int,input().split())
    if str(yi) in y:
        s=s+xi
        y.remove(str(yi))
        
print(s)

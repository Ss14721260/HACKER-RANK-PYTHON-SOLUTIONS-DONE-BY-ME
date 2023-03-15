# Enter your code here. Read input from STDIN. Print output to STDOUT
e=int(input())
re=set(map(int,input().split()))
sf=int(input())
rf=set(map(int,input().split()))
s=len((re.union(rf)).difference(re.intersection(rf)))
print(s)

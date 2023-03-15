# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
rn=list(map(int,input().split()))
sm=(sum(set(rn))*k-(sum(rn)))//(k-1)
print(sm)

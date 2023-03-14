# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())

i=1
for j in range((m-3)//2,0,-3):
    print(('-'*j).ljust(j)+('.|.'*i).center(i)+('-'*j).rjust(j))
    i+=2
print(('WELCOME').center(m,'-'))
i=i-2
for j in range(3,(m-3)//2+1,3):
    print(('-'*j).ljust(j)+('.|.'*i).center(i)+('-'*j).rjust(j))
    i-=2

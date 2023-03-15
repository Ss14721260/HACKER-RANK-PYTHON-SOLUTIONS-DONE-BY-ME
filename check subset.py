# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    al=int(input())
    a=set(input().split())
    bl=int(input())
    b=set(input().split())
    if a.intersection(b)==a:
        print("True")
    else:
        print("False")

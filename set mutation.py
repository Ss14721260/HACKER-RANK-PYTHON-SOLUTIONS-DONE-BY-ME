# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
h=set(map(int,input().split()))
n2=int(input())
for i in range(n2):
    op_l=input().split()
    r=set(map(int,input().split()))
    if op_l[0]=="intersection_update":
        h.intersection_update(r)
    elif op_l[0]=="update":
        h.update(r)
    elif op_l[0]=="symmetric_difference_update":
        h.symmetric_difference_update(r)
    elif op_l[0]=="difference_update":
        h.difference_update(r)
print(sum(h))

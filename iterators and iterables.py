import itertools as itt
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=input().split()
k=int(input())
l=list(itt.combinations(s,k))
c=0
for i in l:
    if 'a' in i:
        c+=1
print(c/len(l))

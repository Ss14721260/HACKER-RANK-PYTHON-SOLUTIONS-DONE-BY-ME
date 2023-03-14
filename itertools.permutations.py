# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,k=map(str,input().split())
k=int(k)
p=list(permutations(s,k))
p.sort()
for i in p:
    print((''.join(list(i))).upper())

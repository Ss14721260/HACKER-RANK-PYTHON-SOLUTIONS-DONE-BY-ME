# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cr
s,k=map(str,input().split())
l=int(k)
st=s.upper()
p=list(cr(st,l))
p.sort()
ls=[]
for i in p:
    ls.append(list(i))
    for j in ls:
        j.sort()
ls.sort()
for i in ls:
    print(''.join(list(i)),end='\n')

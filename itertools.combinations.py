# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,k=map(str,input().split())
k=int(k)
p=[]
for i in range(1,k+1):
    p+=list(combinations(s,i))
st=[]
    
for j in sorted(p):
    st.append((''.join(list(j))).upper())

v=[]
for w in st:
    n=list(w)
    n.sort()
    v.append(n)
v.sort()
for q in range(1,k+1):
    for l in v:
        if len(l)==q:
            print(''.join(l),end='\n')

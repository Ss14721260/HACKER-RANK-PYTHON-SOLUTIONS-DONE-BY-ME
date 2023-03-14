# Enter your code here. Read input from STDIN. Print output to STDOUT
import math as mh
z=complex(input())
x,y=z.real,z.imag
r=mh.sqrt(x**2+y**2)
thita=mh.acos(x/r)
print(r)
if y<0:
    print(-thita)
else:
    print(thita)

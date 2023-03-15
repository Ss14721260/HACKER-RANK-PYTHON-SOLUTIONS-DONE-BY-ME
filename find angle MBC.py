import math as mh
# Enter your code here. Read input from STDIN. Print output to STDOUT
ab=int(input())
bc=int(input())
thita=round((mh.atan(ab/bc)*180/3.141),3)
if int((str(thita).split('.'))[1])>=500:
    print(str(mh.ceil(thita))+'\xb0')
else:
    print(str(mh.floor(thita))+'\xb0')

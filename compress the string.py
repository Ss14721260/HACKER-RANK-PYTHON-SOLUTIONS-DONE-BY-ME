# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as itt
s=input()
for key,group in itt.groupby(s):
    print('({}, {})'.format(len(list(group)),key),end=" ")

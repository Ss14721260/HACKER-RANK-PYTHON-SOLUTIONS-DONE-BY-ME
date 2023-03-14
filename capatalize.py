

# Complete the solve function below.
def solve(s):
    p=s.split(' ')
    l=[]
    for i in p:
        l.append(i.capitalize()+' ')
        t=''.join(l[0:])
    return t

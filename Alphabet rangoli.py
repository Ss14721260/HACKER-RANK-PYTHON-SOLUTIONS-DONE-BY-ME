def print_rangoli(n):
    # your code goes here
    p='abcdefghijklmnopqrstuvwxyz'
    l=[]
    for i in range(n):
        s='-'.join(p[i:n])
        l.append((s[::-1]+s[1:]).center(4*n-3,'-'))
    print('\n'.join(l[:0:-1]+l))


n = int(input())
s = set(map(int, input().split()))
c=int(input())
while c>0:
    c-=1
    n=input()
    if "pop" in n:
        s.pop()
    elif ("remove" in n):
        s.remove(int(list(n.split())[1]))
    elif ("discard" in n):
        s.discard(int(list(n.split())[1]))
print(sum(s))

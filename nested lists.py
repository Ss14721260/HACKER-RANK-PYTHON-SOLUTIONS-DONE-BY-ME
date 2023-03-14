if __name__ == '__main__':
    d={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name]=score
    l=d.values()
    x=sorted(l)
    k=0
    for i in x:
        if i!=x[0]:
            k=i
            break
    nm=[]
    for j in d.keys():
        if d[j]==k:
            nm.append(j)
    for ii in sorted(nm):
        print(ii)
            
    
    
        
        

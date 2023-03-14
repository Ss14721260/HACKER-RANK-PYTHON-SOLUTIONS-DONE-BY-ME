def minion_game(string):
    # your code goes here
    p=string.upper()
    vowel="aeiou".upper()
    n=len(p)
    c=n*(n+1)//2
    kevin=0
    stuart=0
    for i in range(0,n):
        if p[i] in vowel:
            kevin+=len(s[i:])
    stuart=c-kevin
    if kevin==stuart:
        print('Draw')
    elif kevin>stuart:
        print("Kevin",int(kevin))
    else:
        print("Stuart",int(stuart))
        
    
    


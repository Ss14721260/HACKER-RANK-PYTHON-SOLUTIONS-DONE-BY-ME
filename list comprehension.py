if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst=[]
    abc=[]
    try:
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                    if i+j+k != n:
                        abc=[i,j,k]
                        lst.append(abc)
        print(lst)
    except Exception as e:
        print(e)
                        
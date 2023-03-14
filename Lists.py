if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        choice=input()
        if "insert" in choice:
            p=choice.split(" ")
            list.insert(int(p[1]),int(p[2]))
        elif "append" in choice:
            p=choice.split(" ")
            list.append(int(p[1]))
        elif "sort" in choice:
            list.sort()
        elif "print" in choice:
            print(list)
        elif "remove" in choice:
            p=choice.split(" ")
            list.remove(int(p[1]))
        elif "reverse" in choice:
            list.reverse()
        elif "pop" in choice:
            list.pop()
        else:
            print("invalid choice \nplease enter valid choice ")
        

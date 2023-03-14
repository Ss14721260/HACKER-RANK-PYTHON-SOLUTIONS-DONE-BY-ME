
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    p=0
    for i in arr:
        if i!=arr[-1]:
            p=i
        elif i==arr[-1]:
            break
    print(p)

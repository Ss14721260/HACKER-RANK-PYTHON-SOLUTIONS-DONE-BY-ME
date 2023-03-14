def count_substring(string, sub_string):
    l1=len(sub_string)
    c=0
    for i in range(0,len(string)):
            if (string[i:i+l1]==sub_string):
                c+=1
    return c


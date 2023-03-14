def merge_the_tools(string, k):
    # your code goes here
    t=int(len(string)/k)
    ti=[]
    ui=[]
    for i in range(0,len(string),k):
        ti.append(string[i:i+k])
    for j in ti:
        ui.append("".join([j[i] for i in range(0,len(j)) if (j[i] not in j[0:i])]))
    for l in ui:
        print(l)


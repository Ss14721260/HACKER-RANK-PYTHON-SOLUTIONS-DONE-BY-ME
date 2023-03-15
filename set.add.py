# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
st=[]
for i in range(n):
    st.append(input())
print(len(set(st)))

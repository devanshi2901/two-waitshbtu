m=100005
fib=set()
def ch():
    global fib
    p,c=0,1
    fib.add(p)
    fib.add(c)
    while c<=m:
        t=c+p
        if t<=m:
            fib.add(t)
        p=c
        c=t


def ca(l,n):
    s=0
    for i in range(n):
        if l[i] in fib:
            s+=l[i]
    if s in fib:
        return True
    else:
        return False
    
    
size=int(input("Enter the size of list :"))
arr=[]
c=0
for i in range(size):
    le=int(input("Enter the list element(must be an element of fibonacci series) :"))
    arr.append(le)
print(arr)
ch()
if ca(arr,size):
    print("Yes")
else:
    print("False")
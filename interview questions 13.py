l=[]
k=[]
n=int(input("Enter the size of list :"))
for i in range(n):
    le=input("Enter the list element :")
    l.append(le)
print("String list is :",l)
for x in l:
    e=float(x)
    k.append(e)
print("String list converted into float is :",k)
print(k)
print("The value of a,b,c satisfying the given condition is :")
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            if (k[i]+k[j]+k[m]>1 and  k[i]+k[j]+k[m]<2):
                print("a=",k[i])
                print("b=",k[j])
                print("c=",k[m])
                
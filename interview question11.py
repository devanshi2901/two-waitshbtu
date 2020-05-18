def mpdt(l,n):
    m=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                mk=l[i]*l[j]*l[k]
                m.append(mk)
    print(max(m))
    

s=int(input("Enter the size of the list :"))
a=[]
for i in range(s):
    le=int(input("Enter the list element :"))
    a.append(le)
print(a)
mpdt(a,s)
  
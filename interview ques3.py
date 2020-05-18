def order(l,n):
    x=0
    for i in range(n):
        for j in range(n-1):
            if l[j]>l[j+1]:
                x=l[j]
                l[j]=l[j+1]
                l[j+1]=x
    if l[0]==0:
        print("There can't be any positive no. smaller than the least no. in this list bcoz the least no. itself is 0")
    else:
        print("The no. just smaller than the least number in the list is %d "%(l[0]-1))

n=int(input("Enter the size of the list :"))
if n==0:
    print("List size is 0..plzz try again..")
l=[]
for i in range(n):
    le=int(input("Enter element %d :"%(i+1)))
    l.append(le)
print(l)
order(l,n)
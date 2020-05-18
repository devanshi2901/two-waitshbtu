n=int(input("Enter the size of the list :"))
l=[]
for i in range(n):
    e=int(input("Enter the element :"))
    l.append(e)
print(l)
x=0
k=int(input("Enter the no. of smallest element to be searched,it should be less than the size of list :"))
for i in range(n):
    for j in range(n-1):
         if l[j]>l[j+1]:
                x=l[j]
                l[j]=l[j+1]
                l[j+1]=x
print("The value of required smallest element in the list is :")
print(l[k-1])
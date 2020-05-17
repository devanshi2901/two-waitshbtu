def sort(sa):
    e=[]
    o=[]
    for x in sa:
        if x%2==0:
            e.append(x)
        else:
            o.append(x)
    e.sort()
    o.sort(reverse=True)
    sa=o+e
    print(sa)
    	
    
    
sa1=[]
n=int(input("Enter the size of array :"))
for x in range(n):
    e=int(input("Enter the array member :"))
    sa1.append(e)
print(sa1)
sort(sa1)
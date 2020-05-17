def shift(list,n):
    t=0
    for x in range(n):
        for y in range(x+1,n):
            if list[x]<list[y]:
               t=list[x]
               list[x]=list[y]
    print(list)          
            
n=int(input("Enter the size of the list :"))
lista=[]
for x in range(n):
    e=int(input("Enter list member \n:"))
    lista.append(e)
print(lista)
shift(lista,n)

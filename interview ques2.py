def segregate0and1(list, n) : 

    count = 0 

  

    for i in range(0, n) : 

        if (list[i] == 0) : 

            count = count + 1

    for i in range(0, count) : 

        list[i] = 0

    for i in range(count, n) : 

        list[i] = 1

          

 

def print_list(r , n) : 

    print( "list after segregation is ",end = "") 

  

    for i in range(0, n) : 

        print(list[i] , end = " ")
  


n=int(input("Enter the size of the list :"))
l=[]
for i in range(n):
    e=int(input("Enter the list element. List element can only be 0 or 1 :"))
    l.append(e)
print(l)
print("List after sorting is:")

      
segregate0and1(l, n) 
print_list(l, n) 

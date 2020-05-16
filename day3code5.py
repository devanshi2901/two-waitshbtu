size1 = int(input("Enter the number of elements that you want to add in your list1:"))
List1=[ ]
print("Enter the elements in your list1 one by one :")
for i in range(size1):
    List1.append(input())
    size2 = int(input("Enter the number of elements that you want to add in your list2:"))
List2=[ ]
print("Enter the elements in your list2 one by one :")
for i in range(size2):
    List2.append(input())
    intersectionList=list(set(List1).intersection(set(List2)))
    print("The intersection of List1 and List2 is : ", intersectionList)
    
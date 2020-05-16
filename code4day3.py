def duplicate(List):
		duplicateList=[ ]
for x in List :
	if x not in duplicateList :
			duplicateList.append(x)
return duplicateList
Size = int(input("Enter the number of elements that you want to add in your list:"))
print("Enter the elements in your list :")
List=[ ]
for x in range(Size):
	List.append(input())
print("List after removing the duplicate element in the list is:",duplicate(List))
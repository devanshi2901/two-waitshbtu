def permutation(List,String=" ")
Set=set(List)
stringList=[ ]
if len(Set)==1 :
String +=" ".join(List)
return list([String])
for x in Set:
List1=list(List)
S=String + x
List1.remove(x)
stringlist.extend(permutation(List1,S))
return stringlist
string=input("Enter the string:")
List=permutation(list(string))
print("All the possible permutation for the givenstring is : "+",".join(List))

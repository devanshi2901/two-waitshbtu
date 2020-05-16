def Sum(List,size,sum):
sumList = []
if size==1:
for x in List:
sumList.append(sum + x)
return sumList
L=list(List)
for x in List :
L.remove(x)
sumList.extend(Sum(L,size-1,sum + x))
return sumList
def summation(List,size):
sumList = list(List)
for i in range(2,size+1):
sumList.extend(Sum(List,i,0))
num=1
while True:
if number not in sumList:
print("The least integer which is not present in the list and also can not be represented as the summation of sub elelments is: ", 
+num)
break
num=num+1
size = int(input("Enter the number of elements that you want to add in your list:"))
List=[]
print("Enter the elements in your list one by one :")
for i in range(size):
    List.append(input())
    summation(List,size)
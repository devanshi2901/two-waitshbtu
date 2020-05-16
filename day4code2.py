l=[ ]
size=int(input("Enter the size of tuple:"))
for i in range(size):
    element=input("Enter the element:")
    l.append(element)
l.sort()
t=tuple(l)
print(t)

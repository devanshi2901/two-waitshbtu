element=dict()
l=""
sl=""
n=int(input("Enter the number of key:value pairs that u wanna enter:"))
for i in range(n):
    print("Enter the key for dictionary:")
    ekey=input()
    print("Enter the value for the dictionary:")
    evalue=input()
    element[ekey]=evalue
print(element)
print("The second largest value in the dictionary is:")
for e in element:
    for e1 in element:
        if (element[e]>element[e1] and e!=e1):
            l=element[e]
for e in element:
    for e1 in element:
        if (element[e]>element[e1] and element[e]<l):
            sl=element[e]
print(sl)
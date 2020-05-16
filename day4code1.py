def countOccurrence(tup, e): 

    dct = {} 

    for i in tup: 

        if not dct.get(i): 

            dct[i] = 0

        dct[i] += 1

    return sum(dct.get(i, 0) for i in e) 

      
l=[ ]
n=int(input("Enter the size :"))
for i in range(n):
    le=input("Enter the element :")
    l.append(le)
tup=tuple(l)
print(tup)
e=input("Enter the element whose occurence is to be printed :")

print(countOccurrence(tup, e)) 
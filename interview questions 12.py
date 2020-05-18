s1=input("Enter string1 :")
s2=input("Enter any string2 :")
l1=[]
l2=[]
c=""
l1=list(s1)
l2=list(s2)
if l1<l2:
    for x in l1:
        for y in l2:
            if x==y:
                c=c+x    
    print(c)
elif l2<l1:
    for x in l2:
        for y in l1:
            if x==y:
                c=c+x    
    print(c)
elif l2==l1:
    print(l1)
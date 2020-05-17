def Knapsack(a,b,v,n):
    if n==0 or a==0:
        return 0
    for x in range(n):
        for y in range(x+1,n):
            if b[x]+b[y]==a:
                return v[x]+v[y]
            
    
v=[]
b=[]
a=int(input("enter the value of maximum weight :"))
n=int(input("enter the number of items:"))
for x in range(n):
    ve=int(input("enter the value:"))
    we=int(input("enter the weight :"))
    v.append(ve)
    b.append(we)
print(v)
print(b)
print("The value for maximum weight is :")
print(Knapsack(a,b,v,n))
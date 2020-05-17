def knapSack(W, wt, val, n): 

  

    

    if n == 0 or W == 0 : 

        return 0

    if (wt[n-1] > W): 

        return knapSack(W, wt, val, n-1)

    else: 

        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 

                   knapSack(W, wt, val, n-1)) 
 
wt=[]
val=[]
W=int(input("enter the value of maximum weight :"))
n=int(input("enter the number of items:"))
for x in range(n):
    v=int(input("enter the value:"))
    w=int(input("enter the weight :"))
    val.append(v)
    wt.append(w)
print(val)
print(wt)

print  (knapSack(W, wt, val, n) )

def spiralPrint(m, n, a) : 
    k = 0; l = 0
      
  
    while (k < m and l < n) : 
          
  
        for i in range(l, n) : 
            print(a[k][i], end = " ") 
              
        k += 1
  

        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 
              
        n -= 1
  
  
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 
              
            m -= 1
          
      
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
              
            l += 1
            
            
r=int(input("Enter the number of rows :"))
c=int(input("Enter the number of columns :"))
a = []
for i in range(0,r):
    er=[]
    print("Enter the value for row %d:"%i)
    for j in range(0,c):
        print("Value for (%d,%d):"%(i,j),end=" ")
        er.append(input("enter :"))
    a.append(er)
print("2D list is :")
for i in range(r):
    for j in range(c):
        print(a[i][j],end="\t")
    print()
print("Spiral form is :")
spiralPrint(r,c,a)

  

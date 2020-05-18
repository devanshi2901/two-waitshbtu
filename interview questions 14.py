def rotateclockwise(A): 
    N = len(A[0]) 
    for i in range(N//2): 
        for j in range(i,N-i-1): 
            temp=A[i][j] 
            A[i][j]=A[N-1-j][i] 
            A[N-1-j][i]=A[N-1-i][N-1-j] 
            A[N-1-i][N-1-j]=A[j][N-1-i] 
            A[j][N-1-i]=temp 
  
def printMatrix(A,n): 
    for i in range(n):
        for j in range(n):
            print(A[i][j],end="\t")
        print()

r=int(input("Enter the number of rows.Rows should be same as columns bcoz it is a square matrix:"))
a=[]
for i in range(0,r):
    er=[]
    print("Enter the value for row %d:"%i)
    for j in range(0,r):
        print("Value for (%d,%d):"%(i,j),end=" ")
        er.append(input("enter :"))
    a.append(er)
for i in range(r):
    for j in range(r):
        print(a[i][j],end="\t")
    print()
print("Rotated List is: :")
rotateclockwise(a)
printMatrix(a,r)


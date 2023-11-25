#matrix
a=int(input("enter no of rows:"))
b=int(input("enter no of columns:"))
mat1=[]
for i in range(a):
    mat1.append([ ]) 
    for j in range(b):
        mat1[i].append(int(input("enter matrix elements")))
print(mat1)

for k in range(len(mat1)):
    for l in range(len(mat1[i])):
      if mat1[i][j]== mat1[j][i]:
          print(f'it is a symmetric matrix')
          break
      else:
         print(f'it is not a symmetric matrix')  
      
            
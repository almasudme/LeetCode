print("rotate image")
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(matrix)
n=len(matrix)



def move(i,j,buffer):
    ito=j0
    jto=n-1-i
        
    temp=matrix[ito][jto]
    matrix[ito][jto]=buffer
    
    return ito,jto,temp
i=0
j=0

for i in range(int(n/2)):
    for j in range(i,n-i-1):
        buffer=matrix[i][j]
        for k in range(4):
            i,j,buffer=move(i,j,buffer)    
        print(matrix)

print(matrix)



'''
Topic: Matrix Multiplication
Based off: Abdul Bari- Frequency Count Method (Lecture on Youtube)
Time Complexity: O(n^3) for Square Matrices
Space Complexity: O(n^2) 
'''

def multiply_matrix(A,B):
    m=len(A)    												#m = number of rows in A
    n=len(A[0])													#n = number of columns in A
    p=len(B[0])													#p = number of columns in B
    product= [[0 for _ in range(p)] for _ in range(m)]			#creates a matrix with m rows and p columns filled with 0
    
    for i in range(m):											#loops over rows of A
        for j in range(p):										#loops over columns of B
            for k in range(n):									#loops over elements in row of A and column of B
                product[i][j]+= A[i][k] *B[k][j]
    
    print (product)

multiply_matrix([[1,2],[3,4]],[[6,8,10],[7,9,11]])				#example 
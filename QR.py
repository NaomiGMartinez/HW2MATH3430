"""
This assignment is due by 11:59pm on 10/29/2021. 

For this assignment you will be writing a python script named QR.py which will
contain several functions. All functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.

The functions you will need to add are

1) A function which implements the unstable version of Gram-Schmidt for reduced QR
factorization. It will
take as it's argument a matrix and will return a list of two matrices. The first
will be Q and the second will be R from the QR factorization described in the
algorithm.

2) A function which implements the stable version of Gram-Schmidt for reduced QR
factorization.It will take as it's argument a matrix and will return a list of 
two matrices. The first will be Q and the second will be R from the QR factorization 
described in the algorithm.

"""
from LA import *
matrix_a = [[1, 1, 1], [1, 1, 0], [1, 0, 0]]

def gram_schmidt_unstable(matrix):
    """Returns the QR decomposition of a matrix

    The function first calculates Q by normalizing the input.
    The function then calculates R by getting the product of
    the transpose of Q by the original matrix
Args:
    matrix: A matrix of numbers stored as a list of lists
            The first dimension is the columns

Returns:
   A list containing Q and R respectively
""" 
    columns = len(matrix)
    rows = len(matrix[0])
    Q = []
    #Calculate Q matrix
    for column in range(columns):
        i = columns - column - 1
        qcolumn = matrix[column]
        while(i < (columns - 1)):
            j = columns - i
            j = j - 1
            product = inner_product(matrix[column], Q[column - j]) 
            pvector = scalar_vector_multiplication(product, Q[column - j])
            for k in range(rows):
                qcolumn[k] = qcolumn[k] - pvector[k]
            i = i + 1
        pnorm = p_norm(qcolumn)
        qcolumn = scalar_vector_multiplication((1/pnorm), qcolumn)
        Q.append(qcolumn)

    R = [[0 for i in range(rows)] for j in range(columns)]
    for i in range(columns):
        for j in range(rows):
            #Sets 0's in lower triangle
            if j > i:
                R[i][j] = 0
            #Not sure if this always works, just something noticed during testing.
            elif i > j:
                R[i][j] = Q[j][columns - i - 1]
            #Sets R[i][j] to inner product of
            else:
                R[i][j] = inner_product(matrix[i], Q[j])
                
    return [Q, R]

def gram_schmidt_stable(matrix):
    """Returns the QR decomposition of a matrix

    The function first creates an orthogonal matrix "v" from
    the original matrix. It then calculates Q by normalizing v.
    The function then calculates R by getting the product of
    the transpose of Q by the original matrix
Args:
    matrix: A matrix of numbers stored as a list of lists
            The first dimension is the columns

Returns:
   A list containing Q and R respectively
""" 
    columns = len(matrix)
    rows = len(matrix[0])
    v = []
    #Create orthogonal matrix "v"
    for column in range(columns):
        vcolumn = matrix[column]
        i = columns - column
        while(i > 0):
            numerator = inner_product(matrix[0], vcolumn)
            denominator = inner_product(matrix[0], matrix[0])
            #!!!Getting ZeroDivisionError even though denominator is not equal to 0!!!
            projection = numerator/denominator
            pvector = scalar_vector_multiplication(projection, matrix[0])
            for j in range(rows):
                vcolumn[j] = vcolumn[j] - pvector[j]
        v.append(vcolumn)
    #Calculate the Q matrix    
    Q = []
    for column in range(columns):
        #Calculate the norm of each column in orthogonal matrix
        Qn = v[column]
        Qn = scalar_vector_multiplication(1/p_norm(v[column]), Qn)
        #Append each normalized column into Q
        Q.append(Qn)

    R = [[0 for i in range(rows)] for j in range(columns)]
    for i in range(columns):
        for j in range(rows):
            #Sets 0's in lower triangle
            if j > i:
                R[i][j] = 0
            #Not sure if this always works, just something noticed during testing.
            elif i > j:
                R[i][j] = Q[j][columns - i - 1]
            #Sets R[i][j] to inner product of
            else:
                R[i][j] = inner_product(matrix[i], Q[j])
                
    return [Q, R]
    
        
QRD = (gram_schmidt_unstable([[1,1,0],[1,0,1],[0,1,1]]))
print(QRD[0])
print(QRD[1])
print("\n")

def test1():
    assert gram_schmidt_unstable(matrix_a) == [[[0.7071067811865475, 0.7071067811865475, 0.0], [0.4082482904638632, -0.40824829046386296, 0.8164965809277261], [-0.5773502691896257, 0.5773502691896258, 0.5773502691896257]], 
                                               [[1.414213562373095, 0, 0], [0.7071067811865475, 1.2247448713915892, 0], [0.7071067811865475, 0.4082482904638632, 1.1547005383792515]]]


#print(gram_schmidt_stable(matrix_a))
#Proof that inner_product does not return 0
#Therefore could not identify cause of ZeroDivisionError
print(inner_product(matrix_a[0], matrix_a[0]))

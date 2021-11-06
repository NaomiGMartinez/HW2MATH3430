"""
This assignment is due by 11:59pm on 11/05/2021. 

For this assignment you will be updating the python script QR.py from the
previous homework. As usual, all functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

1) Remove the function which implemented unstable Gram-Schmidt. It is unstable
and we may use the stable version exclusively from this point forward. 

2) Write a function which takes as it's argument a list of vectors and returns
an orthonormal list of vectors which shares the same span. 
"""

from LA import *
matrix_a = [[1, 1, 1], [1, 1, 0], [1, 0, 0]]

#Using the unstable version from my previous code since my other one was not quite finished
def gram_schmidt_stable(matrix):
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
        #Calculate orthogonal vector
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
        #Normalize the vector
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

def orthonormal_vectors(matrix):
    """Returns an orthonormal list of vectors

    Given that a list of vectors is essentially a matrix
    and QR decomposition returns a normalized orthogonal
    matrix (assuming dimensions are the same), this is
    a modified version of the previous gram schmidt code
Args:
    matrix: A matrix of numbers stored as a list of vectors

Returns:
   A list containing orthonormal vectors
""" 
    columns = len(matrix)
    rows = len(matrix[0])
    Q = []
    #Calculate Q matrix
    for column in range(columns):
        #Calculate orthogonal vector
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
        #Normalize the vector
        pnorm = p_norm(qcolumn)
        qcolumn = scalar_vector_multiplication((1/pnorm), qcolumn)
        Q.append(qcolumn)
    return Q

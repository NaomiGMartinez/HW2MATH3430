"""
This assignment is due by 11:59pm on 11/12/2021. 

For this assignment you will be updating the python script QR.py from the
previous homework. As usual, all functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.

1) Add a function which takes as it's argument a matrix and implements the
Householder Orthogonalization algorithm to calculate the QR
factorization, stored as a list of two matrices Q and R. 
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

def householder_qr(matrix):
    """Returns QR decomposition as a list of two matrices

        Function calculates a series of Householder matrices, multiplying
        them from the left to get R. Once they have all been calculated, Q
        is then calculated by getting the product of all Householder matrices.
    Args:
        matrix: A matrix of numbers stored as a list of vectors

    Returns:
       A list containing matrix Q and matrix R
    """ 
    #Get length of rows and columns and declare variables
    columns = len(matrix)
    rows = len(matrix[0])
    a = matrix
    R = matrix
    hlist = []
    #Begin for loop calculating every h value
    for entryNum in range(columns):
        #Calculate a1
        a1 = 0
        for i in range(len(a[0])):
            a1 = a1 + a[0][i] ** 2
        a1 = a1 ** (1/2)
        #Create the identity matrix
        identity = [[0 for element in range(len(a))] for element in range(len(a[0]))]
        for i in range(len(a)):
            identity[i][i] = 1
        #Calculate v
        e1 = scalar_vector_multiplication(a1, i[0])
        v = add_vectors(a[0], e1)
        #Start householder transformation
        numerator = inner_product(v, v)
        numerator = numerator * 2
        denominator = inner_product(v, v)
        fraction = numerator / denominator
        if fraction < 0:
            fraction = fraction * -1
        h = identity
        #Subtract h from the identity matrix
        for i in range(columns):
            for j in range(rows):
                h[i][j] = identity[i][j] - fraction
        #Multiply h by a
        a = matrix_multiplication(h, a)
        #Calculate final value of h       
        if len(h[0]) > columns:
            h = [[0 for element in range(rows)] for element in range(columns)]
            for i in range(columns):
                identity[i][i] = 1
            difference = columns - entryNum
            for i in range(len(h)):
                for j in range(len(h[0])):
                    h[i+difference][j+difference] = a[i][j]
        else:
            h = a
        #Add h to hlist
        hlist.append(h)
        #Update the value of R
        R = matrix_multiplication(h, R)
        #Remove the first row and column from result h to get a
        result = [[0 for element in range(columns - 1)] for element in range(rows - 1)]
        for i in range(len(a) - 1):
            for j in range(len(a) - 1):
                result[i][j] = a[i + 1][j + 1]        
        a = result
    #Calculate Q by iterating through R
    Q = [[[1 for element in range(columns)] for element in range(rows)]]
    for entry in range(hlist):
        Q = matrix_multiplication(Q, hlist[entry])

    return [Q, R]

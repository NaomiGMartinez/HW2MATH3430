"""
This assignment is due by 11:59pm on 11/28/2021. 

For this assignment you will be writing a python script named LS.py which will
contain several functions. All functions must satisfy the same requirements as in HW03. 

You will import the LA.py and QR.py scripts from the previous homeworks. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.

The functions you will need to write are

1) Write a function which takes as it's argument a vector stored as a list, and
a matrix, and returns the least squares solution, calculated by using QR
factorization.
"""
 
from LA import *
from QR import *

def least_squares(vector, matrix):
    """Returns the least squares solution of a vector and a matrix using a modified version
        of the formula Ax ~ b and x = (A^(T)A)^(-1)A^(T)b and A = QR
    
        The function first calculates the QR factorization using gram-schmidt
        Then the function calculates the right side of the equation Rx = Q^(T)b
        The function then returns the solution using the back_substitution function
        given in class.

    
    Args:
        matrix: A matrix of numbers stored as a list of lists
        The first dimension is the columns. (A)
        vector: A vector stored as a list of numbers (b)

    Returns:
       Returns the least squares solution
    """ 
    #Get QR decomposition of given matrix
    qr = gram_schmidt_stable(matrix)
    Q = qr[0]
    Q = matrix_vector_multiplication(Q, vector)
    R = qr[1]
    return back_substitution(R, Q)

#Code provided in class
def back_substitution(matrix: list, vector: list) -> list:
    #Initialize result as our first solution in back substitution.
    result: list = [vector[-1]*(1/(matrix[-1][-1]))]
    #Iterate from second to last column to the first column
    for current in range(len(matrix) -1, -1, -1):
        #Set temp to be current element from vector
        temp: float = vector[current]
        #Subtract previous solutions, scaled by their coefficients in the
        #Corresponding equation from temp.
        for index in range(len(result)):
            temp -= matrix[len(matrix)-1-index][current]*result[current]
        #Divide temp by the coefficient of the variable we are solving for from
        #the corresponding equation.
        temp *= 1/(matrix[current][current])
        #Append newly found solution to result
        result.append(temp)
    #Reverse the order of solutions, to obtain our desired solution vector
    result = result[::-1]
    return result


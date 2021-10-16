"""
This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are 

#0 A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.


#1 A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.


#2 A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.

#3 A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.

#4 A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.

#5 A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""

vector_a = [1, 2, 3]
matrix_a = [[1, 2], [3, 4],[5, 6]]
matrix_b = [[1, 2, 3], [4, 5, 6]]

# Begin Example
# Problem #0

def add_vectors(vector_a: list[float],
                vector_b: list[float]) -> list[float]:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# End Example
# Note that you must add unit tests for problem 0!!!!!

def test_0():
    assert add_vectors(vector_a, vector_a) == [2, 4, 6]

#Problem 01

def scalar_vector_multiplication(scalar, vector):
  
"""Multiply the elements in a vector by the scalar.

   Creates a result vector the same size as the given vector which contains only 0's.
   It then loops over the given vector and multiplies each element in the vector by the scalar
   and places the result in the new vector in the same index as the corresponding element
   in the given vector. After it breaks the loop, it returns the resulting vector.

    Args:
    scalar: A integer.
    vector: A vector stored as a list.
    
    Returns:
      A result vector that is the product of the scalar and the given vector.
    """

    result = [0 for element in vector]
    
    for x in range(len(vector)):
        result[x] = vector[x] * scalar
    return result

def test_1():
    assert scalar_vector_multiplication(2, vector_a) == [2, 4, 6]

#Problem 2

def scalar_matrix_multiplication(scalar, matrix):

"""Multiply the elements in the matrix by the scalar.

   Creates a result matrix the same size as the given matrix which contains only 0's.
   It then loops over the matrix and multiplies the element in the matrix by the scalar
   and places the result in the new matrix in the same index as the corresponding elements
   in the given matrix. After it breaks the loop, it returns the resulting matrix.
   
   Args:
       scalar: A integer.
       matrix: A matrix stored as a list of lists.
       
   Result:
          A result matrix that is the product of the scalar and the given matrix.
"""



    result = [[0 for element in range(len(matrix[0]))] for element in range(len(matrix))]

    for row in range(len(matrix)):
         for column in range(len(matrix[0])):
             result[row][column] = matrix[row][column] * scalar

    return result

def test_2():
    assert scalar_matrix_multiplication(2, matrix_a) == [[2, 4], [6, 8], [10, 12]]

# Problem 3

def matrix_addition(matrix_a, matrix_b):

"""Adds two input matrices
   
   Creates a result matrix of the same size as one of the input matrices. 
   It then loops over the matrices and adds  the elements in matrix_a by matrix_b
   and places the result in the new matrix in the same format as the corresponding elements
   in the given matrix. After it breaks the loop, it returns the resulting matrix.
   
   Args:
       matrix_a: a matrix stored as a list of lists.
       matrix_b: a matrix, the same size as matrix_b stored as a list of lists.
       
    Result:
       A result matrix that contains the sum of the two given matrices.
"""

    result = [[0 for element in range(len(matrix_a[0]))] for element in range(len(matrix_a))]

    for row in range(len(matrix_a)):
        for column in range(len(matrix_a[row])):
             result[row][column] = matrix_a[row][column] + matrix_b[row][column]

    return result


def test_3():
    assert matrix_addition(matrix_a, matrix_a) == [[2, 4], [6, 8], [10, 12]]

# Problem 4

def matrix_vector_multiplication(matrix, vector):

"""Gets the product of an input matrix and an input vector

   Creates a result matrix of the same size as one of the input matrices. 
   It then loops over the matrix and vector and multiplies the corresponding elements
   and places the result in the new matrix in the same format as the corresponding elements
   in the given matrix. After it breaks the loop, it returns the resulting matrix.   

   Args:
       matrix: matrix_a stored as a list of lists.
       vector: a vector, same length as an element in the matrix (A list in the list of lists)
       
    Result:
       A result matrix that contains the product of the two given argument.

"""

    result = [[0 for element in range(len(matrix[0]))] for element in range(len(matrix))]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            result[row][column] = matrix[row][column] * vector[column]

    return result

def test_4():
    assert matrix_vector_multiplication(matrix_b, vector_a) == [[1, 4, 9], [4, 10, 18]]

# Problem 5

def matrix_multiplication(matrix_a, matrix_b):

"""Gets the product of two input matrices

   Creates a result matrix of the same number of rows in matrix_a and the same number of columns as matrix_b. 
   It then loops over the matrices and multiplies the corresponding elements
   and adds the result to the element in the corresponding location of the result matrix.
   After it breaks the loop, it returns the resulting matrix.   

   Args:
       matrix_a: a matrix stored as a list of lists.
       matrix_b: a matrix stored as a list of lists whos rows must equal matrix_a's columns.
       
    Result:
       A result matrix that contains the product of the two given matrices.

"""

    result = [[0 for element in range(len(matrix_b[0]))] for element in range(len(matrix_a))]

    for x in range(len(matrix_a)):
    	for y in range(len(matrix_b[x])):
    		for z in range(len(matrix_b)):
    			result[x][y] = result[x][y] + matrix_a[x][z] * matrix_b[z][y]

    return result

def test_5():
    assert matrix_multiplication(matrix_b, matrix_a) == [[22, 28], [49, 64]]
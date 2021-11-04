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

import math
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

#Problem 01

def scalar_vector_multiplication(scalar, vector):

    result = [0 for element in vector]
    
    for x in range(len(vector)):
        result[x] = vector[x] * scalar
    return result

#Problem 2

def scalar_matrix_multiplication(scalar, matrix):

    """
    docstring goes here
    """

    result = [[0 for element in range(len(matrix[0]))] for element in range(len(matrix))]

    for row in range(len(matrix)):
         for column in range(len(matrix[0])):
             result[row][column] = matrix[row][column] * scalar

    return result

# Problem 3

def matrix_addition(matrix_a, matrix_b):

    """
    docstring goes here
    """

    result = [[0 for element in range(len(matrix_a[0]))] for element in range(len(matrix_a))]


    for row in range(len(matrix_a)):
        for column in range(len(matrix_a[row])):
             result[row][column] = matrix_a[row][column] + matrix_b[row][column]

    return result

# Problem 4

def matrix_vector_multiplication(matrix, vector):

    """
    women do not know how to use computers
    """

    result = [[0 for element in range(len(matrix[0]))] for element in range(len(matrix))]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            result[row][column] = matrix[row][column] * vector[column]

    return result

def matrix_multiplication(matrix_a, matrix_b):

    """
    docstring goes here
    """

    result = [[0 for element in range(len(matrix_b[0]))] for element in range(len(matrix_a))]

    for x in range(len(matrix_a)):
        for y in range(len(matrix_b[x])):
            for z in range(len(matrix_b)):
                result[x][y] = result[x][y] + matrix_a[x][z] * matrix_b[z][y]

    return result

"""
This assignment is due by 11:59pm on 10/22/2021. 

For this assignment you will be adding functinos to the LA.py script from HW03.
All functions must satisfy the same requirements as in HW03. The functions you
will need to add are

#1) A function which takes a scalar as it's input and returns it's absolute
value. Note that this function must be able to take both real numbers and
complex numbers as input!!!



#2) A function which takes the as it's arguments

1) A vector stored as a list.

2) A float valued scalar, set to default as 2. 

and returns the p-norm of the input vector. Which p-norm must be determined using
the float valued scalar input. If no argument is given, it should default to
2. 

#3) A function which takes as it's argument a vector stored as a list and
returns the infinity norm of the input vector.

#4) A function which takes as it's arguments

1) A vector stored as a list.

2) An float valued scalar, set to default as 2.

3) A boolean value, set to default as False.

The function will return the p-norm of the input vector. If the boolean value is
given as True, the function will return the infinity norm of the input vector.
Otherwise it will return the p-norm of the vector corresponding to the float 
scalar argument. This function must use the functions from problem #2 and
problem #3 to earn credit. 

#5) A function which takes as it's arguments two vectors, stored as lists. This
function then returns the inner product of these vectors. Your function must be
able to handle complex numbers!
"""

"""Returns the abolute value of the input scalar.

This function first checks wether the input is a complex number. If so,
it will return the square root of the sum of the real number squared
and the imaginary numbere squared. Otherwise, it will check wether the
numeric value is 0 or greater, in which case it will return that same
number. Finally, it will return the scalar multiplied by -1 as a final
option.

Args:
    scalar: A numerical value or complex number.

Returns:
   An float. 
""" 

def absolute_value(scalar):
    #Checks if complex
    if type(scalar) is complex:
        return math.sqrt((scalar.real ** 2) + (scalar.imag ** 2))
    #Checks if scalar is positive or negative
    elif scalar >= 0:
        return scalar
    else:
        return scalar * -1

"""Returns the pnorm of the input vector.

This loops through the input vector and adds each element
(to the power of the scalar) to the total. The total to the
power of 1 over the input scalar is then returned.

Args:
    vector: A vector of numbers stored as a list
    scalar: A numerical value set to 2 by default.

Returns:
   A float.
""" 

def p_norm(vector, scalar = 2):
    #Gets length for loop
    length = len(vector)
    #Return value
    total = 0
    #Loops through vector
    for i in range(length):
        #Firt calculates the value that will be added to total
        addition = vector[i]**scalar
        #Adds assition to return value
        total = total + addition
    #Calculates the final return value, which is total to the power of 1 over scalar
    total = total**(1/scalar)
    #Returns total
    return total

"""Returns the infinity norm of the input vector.

This loops through the input vector and adds the absolute
value of that element to the total. It then returns the total.

Args:
    vector: A vector of numbers stored as a list

Returns:
   A float.
""" 

def infinity_norm(vector):
    #Gets length of vector for loop
    length = len(vector)
    #Innitializes return value
    total = 0
    #Loops through input vector
    for i in range(length):
        #Adds absolute value to return value
        total = total + absolute_value(vector[i])
    #Returns total
    return total

"""Returns the p norm or infinity norm of the input vector.

This function simply check wether infinite is set to True or False.
If it is True, it will call infinity_norm() and pass any relevant
input values as parameters. Otherwise, it will do the same but to p_norm()

Args:
    vector: A vector of numbers stored as a list
    scalar: A numerical value set to 2 by default.
    infinite: A boolean set to fale by default.

Returns:
   A float.
""" 

def norm(vector, scalar = 2, infinite = False):
    #Checks if infinite is true
    if(infinite == True):
        #Returns infinity norm by calling function
        return infinity_norm(vector)
    #Defaults to false
    else:
        #Returns p norm by calling function
        return p_norm(vector, scalar)

"""Returns the inner product of 2 input vectors.

This loops through both vectors simultaniously and adds
the product of both elements in the same index on the two
vectors to the variable total. It then returns total. If
the vectors are not the same length, it will return -1
(As a form of error checking)

Args:
    vectorA: A vector of numbers stored as a list
    vectorB: A vector of numbers stored as a list.
             Must be equal in length to vectorA

Returns:
   A float.
""" 

def inner_product(vectorA, vectorB):
    #Innitiates return value
    total = 0
    #Checks if input vectors are of equal length
    if(len(vectorA) != len(vectorB)):
        #Returns error value
        return -1
    #Gets length of vectorA for the loop
    length = len(vectorA)
    #Loops through both vectors simultaneously
    for i in range(length):
        #Adds product of both elements to return value
        total = total + (vectorA[i] * vectorB[i])
    #Returns total
    return float(total)

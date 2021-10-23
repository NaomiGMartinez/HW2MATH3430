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

#Math is required for certain methods
import math
#Just an example complex number
x = complex(3, 4)

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

#Test for complex number
def test_1():
    assert absolute_value(x) == 5
#Test for negative number
def test_2():
    assert absolute_value(-5) == 5

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

#Tests with simple vector
def test_3():
    assert p_norm([1, 2, 3]) == 3.7416573867739413

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

#Tests with simple vector
def test_4():
    assert infinity_norm([1, 2, 3]) == 6

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

#Tests with default value
def test_5():
    assert norm([1, 2, 3]) == 3.7416573867739413

#Tests with input values
def test_6():
    assert norm([1, 2, 3], 2, True) == 6

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
    return total

#Tests with simple vectors
def test_7():
    assert inner_product([1, 2, 3], [1, 1, 1]) == 6
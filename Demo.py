
"""
For your final project you will make a folder called "final_Project" in your
github repo. In this folder you will write 7 python scripts with the following
names.

LA.py
test_LA.py
QR.py
test_QR.py
LS.py
test_LS.py
Demo.py

For every function you write in your scripts they must

1) Use type annotations as discussed in class. 

2) Have a corresponidng doc string using the format discussed in class.

3) have a test in the corresponding pytest script. 

Note: In the work below, all matrices are stored as lists of lists, where each
component list represents a column of the matrix. You must use this
representation for matrices. Similarly, all vectors are stored as lists. 

Note: You are free to write additional functions in order to meet the
requirements specified below. 

--------------------------------------------------------------------------------
Specifications for LA.py
--------------------------------------------------------------------------------
LA.py must include the following functions.

#0 A function which takes two vectors as its arguments and returns their sum. 

#1 A function which takes as its arguments a scalar and a vector, then returns
the corresponding scalar-vector multiplication.

#2 A function which takes a scalar and a matrix as its arguments, and returns
the corresponding scalar-matrix multiplication. This function must use the
function written for #1! Failure to use this function will result in an earned
grade of 0 for this problem. 

#3 A function which takes two matrices as its arguments and returns their
sum. This function must use the function from #0. Failure to use this function
will result in an earned grade of 0 for this problem.

#4 A function which takes a matrix and a vector as its arguments and returns the
corresponding matrix-vector multiplication. This function must use the linear
combination of columns method discussed in class. All other methods are
considered invalid. Additionally, this function must use the functions from #0
and #1. Failure to meet these requirements will result in an earned grade of 0
for this problem.

#5 A function which takes two matrices as its arguments and returns their
product. This function must use the function from #4 and implement the
matrix-vector multiplication approach to matrix-matrix multiplication. Failure
to meet these requirements will result in an earned grade of 0 for this problem.

#6 A function which takes a vector and a float as its arguments, with the float
defaulting to 2. The function must then return the p-norm of the vector where p
is determined using the float.  

#7 A function which takes a vector as its argument and returns the infinity norm
of the vector.

#8 A function which takes a vector, a float which defaults to 2, and a boolean
value which defaults to False. The function will return the p-norm of the vector
determined by the float and the boolean. If the boolean is True, then the
function returns the infinity norm of the vector. If the boolean is False, then
the function returns the p-norm of the vector where p is determined by the
float. This function must use the functions from #6 and #7. 

#9 A function which takes two vectors as its argument and returns their inner
product. Note that the function must be able to handle complex valued vectors.  

--------------------------------------------------------------------------------
Specifications for test_LA.py
--------------------------------------------------------------------------------

#10 A pytest for each function in LA.py. That test must include at
least two asserts. 

--------------------------------------------------------------------------------
Specifications for QR.py
--------------------------------------------------------------------------------

#11 A function which takes a matrix as its argument and implements the stable 
version of Gram-Schmidt for reduced QR factorization. The function will then
return the matrices Q and R stored as a list. i.e. [Q,R] 

#12 A function which takes a list of vectors as its argument and returns an
orthonormal list of vectors which shares the same span. 

#13 A function which takes a matrix as its arguments and implements Householder
Orthogonalization to calculate the QR factorization. The function will then
return the matrices Q and R stored as a list.  

--------------------------------------------------------------------------------
Specifications for test_QR.py
--------------------------------------------------------------------------------

#14 A pytest for each function in QR.py. That test must include at
least two asserts. 
 

--------------------------------------------------------------------------------
Specifications for LS.py
--------------------------------------------------------------------------------

#15 A function which takes a matrix and a vector as its arguments and returns
the corresponding least squares solution, calculated by using the QR
factorization method discussed in class.   

--------------------------------------------------------------------------------
Specifications for test_LS.py
--------------------------------------------------------------------------------

#16 A pytest for each function in LS.py. That test must include at least two
asserts. 

--------------------------------------------------------------------------------
Specifications for Demo.py
--------------------------------------------------------------------------------

In Demo.py you will not be writing any functions. Instead you will be
demonstrating the functionality of the library you've written. 

Begin by writin a print statement that introduces yourself and the library
you've written.

For each function in LA.py, QR.py, and LS.py 

1) Write a print statement which introduces the function and what it does. 

2) Write a print statement which introduces an example (I suggest reusing one of
your tests.) 

3) Write a print statement which prints the example. 

for example

################################################################################

print("LA.py contains a large number of functions for performing basic linear
algebra tasks.")
print("The first function in LA.py is add_vectors. It will take in two vectors
as its arguments and return their sum.")

print("For example, if a = [1,2] and b = [3,4], then add_vectors(a,b) will
return")


a = [1,2]
b = [3,4]
print(LA.add_vectors(a,b))

################################################################################
"""

from LA import *
from LS import *
from QR import *

scalar_1=2
scalar_2=-2
vector_a=[1,2,3]
vector_b=[2,4,6]
vector_c=[3,9,0]
matrix_a=[[1,2],[3,4],[5,6]]
matrix_b=[[1,2,3],[4,5,6]]
matrix_c=[[1,2,1],[2,3,3],[4,1,2]]
matrix_d=[[2,1,2],[1,1,1]]

print("Hello World! My name is Naomi, and this is the library I have created.\n")

print('''Within this library, it consists of several linear algebraic tecniques than can be found in LA.py, QR.py, and LS.py.
I will begin by demonstrating the elemetary linear albebraic operations found in LA.py:\n''')


print('''add_vectors is the first function in LA.py. 
This will use the two input vectors as its argument and return the final sum of the vectors:''')
print("For instance, if we have vector_a=[1,2,3] add_vectors(vector_a, vector_a) will return:")
print(add_vectors(vector_a, vector_a))
print(" ")

print('''For the second function scalar_vector_multiplication found in LA.py, you 
will be multiplying the elements in a vector by the scalar given as argument 
that returns a result vector as a product of the scalar and the given vector:''')
print('''For example, if we have scalar_1=2 and vector_a=[1,2,3], scalar_vector_multiplication(vector_a, scalar_1) returns:''')
print(scalar_vector_multiplication(vector_a,scalar_1))
print(" ")

print('''For the third function scalar_matrix_multiplication found in LA.py, it will use as input a matrix and 
a scalar and return a matrix that is the final product of the given scalar and matrix:''')
print('''For example, if we have scalar_1=2 and matrix_a=[[1,2],[3,4],[5,6]] then scalar_matrix_multiplication(scalar_1, matrix_a) returns:''')

print(scalar_matrix_multiplication(scalar_1,matrix_a))
print(" ")

print('''For the fourth function matrix_addition found in LA.py, it will add two input matrices and return a matrix of
the sum of the two given matrices:''')
print('''For instance if we have matrix_a=[[1,2],[3,4],[5,6]] then matrix_addition(matrix_a, matrix_a) returns''')
print(matrix_addition(matrix_a, matrix_a))
print(" ")

print('''In the fifth function matrix_vector_multiplication found in LA.py, it will use as input a matrix and a vector that returns the product
of the two given arguments:''')
print('''For example, if we have matrix_b=[[1,2,3],[4,5,6]] and vector_a=[1,2,3], matrix_vector_multiplication(matrix_b, vector_a) returns:''')
print(matrix_vector_multiplication(matrix_b, vector_a))
print(" ")

print('''In the sixth function matrix_multiplication found in LA.py, it will take two matrices as input, then return their
product as a matrix''')
print('''For example, given matrix_a=[[1,2],[3,4],[5,6]] and matrix_b=[[1,2,3],[4,5,6]], matrix_multiplication(matrix_a, matrix_b) returns''')
print(matrix_multiplication(matrix_a, matrix_b))

print('''For the seventh function absolute_value found in LA.py it first checks whether the input is a complex number, positive number, or negative
number and returns the absolute value for that number:''')
print('''For example, if we have scalar_2=-2, absolute_valuez(scalar_b) will return:''')
print(absolute_value(scalar_2))
print(" ")

print('''In the eigth function, p_norm in LA.py it uses as it's arguments a vector and a scalar of numerical value set to 2 that returns a float. This
function can be used for both complex and real numbers:''')
print('''For example if we have vector_a=[1,2,3], the result of p_norm(vector_a) is:''')
print(p_norm(vector_a))
print(" ")

print('''For the ninth function infinity_norm in LA.py it will return the infitity_norm of the input vector:''')
print('''For example, if we have vector_3=[2,4,6], the result of infinity_norm(vector_3) is:''')
print(infinity_norm(vector_b))
print(" ")

print('''For the tenth function, norm, in LA.py is uses as it's arguments a vector, a scalar of numerical value set to 2, and a boolean initially set
to false: If the boolean is false, it will call p_norm, otherwise it will call infinity_norm:''')
print('''For example if we have vector_a=[1,2,3] the result of norm(vector_a) is:''')
print(norm(vector_a))
print(" ")

print('''The eleventh function inner_product found in LA.py serves to return the inner product of two input vectors:''')
print('''For example, if we have vector_a=[1,2,3] and vector_b=[2,4,6] the result is:''')
print(inner_product(vector_a, vector_b))
print(" ")

print('''Correspondingly, I will provide a demonstration of the various functions from QR.py:\n''')

print('''The first function, gram_schmidt_stable in QR.py uses as it's argument a matrix and returns the QR decomposition of the input:''')
print('''For example, if we have matrix_c=[[1,2,1],[2,3,3],[4,1,2]], the result of gram_schmidt_stable is:''')
print(gram_schmidt_stable(matrix_c))
print(" ")

print('''The second function orthonormal_vectors in QR.py uses as it's argument a matrix and returns a list containing orthonormal vectors:''')
print('''For example, if we have matrix_c=[[1,2,1],[2,3,3],[4,1,2]] the result of orthonormal_vectors(matrix_c) is''')
print(orthonormal_vectors(matrix_c))
print(" ")

print('''The third function householder_qr in QR.py uses as it's argument a matrix that returns its QR factorization:''')
print('''For example, if we have matrix_c=[1,2,1],[2,3,3],[4,1,2]] the result of householder_qr(matrix_c) is:''')
print(householder_qr(matrix_c))
print(" ")

print('''Lastly, I will now demonstrate the functions found in LS.py\n''')

print('''The first function least_squares in LS.py uses as it's arguments a matrix and a vector and returns the least squares solution:''')
print('''For example, if we have matrix_d=[[2,1,2],[1,1,1]] and vector_c=[3,9,0], least_squares(vector_c, matrix_d) returns''')
print(least_squares(vector_c, matrix_d))
print(" ")

print('''This summarizes my library.Thank you, goodbye!''')
print(" ")
from LA import *

def test_add_vectors():
    vector_a = [1, 2, 3]
    vector_b = [2, 4, 6]
    assert add_vectors(vector_a, vector_a) == [2, 4, 6]
    assert add_vectors(vector_a, vector_b) == [3, 6, 9]

def test_scalar_vector_multiplication():
    vector_a = [1, 2, 3]
    vector_b = [2, 4, 6]
    scalar_a = 2
    assert scalar_vector_multiplication(scalar_a, vector_a) == [2, 4, 6]
    assert scalar_vector_multiplication(scalar_a, vector_b) == [4, 8, 12]

def test_scalar_matrix_multiplication():
    matrix_a = [[1, 2], [3,4], [5, 6]]
    matrix_b = [[1, 2, 3], [4, 5, 6]]
    scalar_a = 2
    scalar_b = 3
    assert scalar_matrix_multiplication(scalar_a, matrix_a) == [[2, 4], [6, 8], [10, 12]]
    assert scalar_matrix_multiplication(scalar_b, matrix_b) == [[2, 4, 6], [8, 10, 12]]

def test_matrix_addition():
    matrix_a = [[1, 2], [3, 4], [5, 6]]
    matrix_b = [[1, 2, 3], [4, 5, 6]]
    assert matrix_addition(matrix_a, matrix_a) == [[2, 4], [6, 8], [10, 12]]
    assert matrix_addition(matrix_b, matrix_b) == [[2, 4, 6], [8, 10, 12]]

def test_matrix_vector_multiplication():
    matrix_b = [[1, 2, 3], [4, 5, 6]]
    matrix_c = [[1, 2], [2, 4]]
    vector_a = [1, 2, 3]
    vector_c = [1, 3]
    assert matrix_vector_multiplication(matrix_b, vector_a) == [[1, 4, 9], [4, 10, 18]]
    assert matrix_vector_multiplication(matrix_c, vector_c) == [[8, 14]

def test_matrix_multiplication():
    matrix_a = [[1, 2], [3, 4], [5, 6]]
    matrix_b = [[1, 2, 3], [4, 5, 6]]
    matrix_c = [[1, 2], [2, 4]]
    assert matrix_multiplication(matrix_b, matrix_a) == [[22, 28], [49, 64]]
    assert matrix_multiplication(matrix_c, matrix_b) == [[9, 12, 15], [19, 26, 33]]

def test_absolute_value():
    scalar_1 = -2
    scalar_2 = 4 + 3j
    assert absolute_value(scalar_1) == 2
    assert absolute_value(scalar_2) == 5
   
def test_p_norm():
    vector_a = [1, 2, 3]
    assert p_norm(vector_a) == 3.7416573867739413
    assert p_norm(vector_a, 1) == 6
   
def test_infinity_norm():
    vector_a = [1, 2, 3]
    vector_b = [2, 4, 6]
    assert infinity_norm(vector_a) == 3
    assert infinity_norm(vector_b) == 6

def test_norm():
    vector_a = [1, 2, 3]
    vector_d = [3, 2, 1]
    assert norm(vector_a, 2) == 3.7416573867739413
    assert norm(vector_d, 2, True) == 3

def test_inner_product():
    vector_a = [1, 2, 3]
    vector_b = [2, 4, 6]
    vector_e = [1, 2j, 3]
    vector_f = [3j, 2, 1]
    assert inner_product():
    assert inner_product(vector_a, vector_b) == 28
    assert inner_product(vector_e, vector_f) == 7j+3
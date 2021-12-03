
vector_a = [1, 2, 3]
matrix_a = [[1, 2], [3, 4],[5, 6]]
matrix_b = [[1, 2, 3], [4, 5, 6]]

def test_0():
    assert add_vectors(vector_a, vector_a) == [2, 4, 6]

def test_1():
    assert scalar_vector_multiplication(2, vector_a) == [2, 4, 6]

def test_2():
    assert scalar_matrix_multiplication(2, matrix_a) == [[2, 4], [6, 8], [10, 12]]

def test_3():
    assert matrix_addition(matrix_a, matrix_a) == [[2, 4], [6, 8], [10, 12]]

def test_4():
    assert matrix_vector_multiplication(matrix_b, vector_a) == [[1, 4, 9], [4, 10, 18]]

def test_5():
    assert matrix_multiplication(matrix_b, matrix_a) == [[22, 28], [49, 64]]
from LS import *

def test_least_squares():
    matrix_d = [[2, 1, 2], [1, 1, 1]]
    matrix_b = [[2, 1, 1], [1, 2, 1]]
    vector_c = [3, 9, 0]
    vector_b = [2, 0, -3]
    assert least_squares(vector_c, matrix_d) == [5, 7.77817459]
    assert least_squares(vector_b, matrix_b) == [1, -1]
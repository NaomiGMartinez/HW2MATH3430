from LS.py import* 

def test_1():
    assert LS.least_squares([[2,1,2][1,1,1]],[-9,3,0]) ==[-15/2, 21/2]

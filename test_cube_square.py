from cube_square import cube_square
def test_normal_numbers():
    assert cube_square(2)==(4,8)
def test_negative_numbers():
    assert cube_square(-3)==(9,-27)
def test_zero():
    assert cube_square(0)==(0,0)

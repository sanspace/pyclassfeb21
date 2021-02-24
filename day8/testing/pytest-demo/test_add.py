from add import add

def test_can_add_numbers():
    assert add(2,3) == 5

def test_can_add_negative_numbers():
    assert add(-2,-5) == -7

def test_negative_assert():
    assert add(2,3) != 6

def test_can_concatenate_strings():
    assert add('hi', 'there') == 'hithere'

def test_can_add_lists():
    assert add([1,2,3], [4,5]) == [1, 2, 3, 4, 5]


from add import add
import pytest

@pytest.mark.parametrize(
    "element1,element2,expected",
    [
        (2,3,5),
        (-2,-5,-7),
        ([1,2,3],[4,5],[1,2,3,4,5]),
        ('hi','there','hithere'),
    ]
)
def test_add_elements(element1, element2, expected):
    assert add(element1, element2) == expected

def test_negative_assert():
    assert add(2,3) != 6


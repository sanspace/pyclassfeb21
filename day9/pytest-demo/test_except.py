import pytest

@pytest.mark.skip(reason="We don't want to test this")
def test_zero_division():
    with pytest.raises(ValueError):
        1 / 0
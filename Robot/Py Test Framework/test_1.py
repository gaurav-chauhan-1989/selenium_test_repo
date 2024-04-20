import pytest

@pytest.mark.dependency()
def test_case1(URL):
    print('This is case 1')
    assert 2==2

@pytest.mark.dependency(depends = ["test_case1"])
def test_case2(URL):
    print('This is case 2')


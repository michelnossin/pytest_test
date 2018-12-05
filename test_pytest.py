import pytest
from pytest import approx, raises


def setup_module():
    print(f"setup in module")


def teardown_module():
    print(f"teardown in module")


def setup_function(function):
    print(f"setup in function {function}")


def teardown_function(function):
    print(f"teardown in function {function}")


def leapYear(year):
    return True


def get_six():
    return 6


def test_can_assert_true():
    leapYear(1)


def test_some_float():
    x = 0.1
    assert (x + 0.2) == approx(0.3)


def raise_exception():
    print("raise exception")
    raise ValueError


def test_exception():
    with raises(ValueError):
        raise_exception()


def test_willSixbeSix():
    my_number = get_six()
    assert my_number == 6


def ignore_this():
    assert 1 == 2


@pytest.mark.michel
def test_marked_test():
    print("A marked test to run within pytest -m")
    assert True


class TestSomeTests:
    @classmethod
    def setup_class(cls):
        print("setup class")

    @classmethod
    def teardown_class(cls):
        print("teardown class")

    def test_one(self):
        print("Test one")
        assert 1 == 1

    def test_two(self):
        print("test two")
        assert 2 == 2

    def also_this_runs_test(self):
        print("not shown")
        assert 1 == 2

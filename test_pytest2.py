import pytest


@pytest.fixture(scope="session", autouse=True, params=[1, 2])
def run_before_session(request):
    print("Running before session")
    print(f"value {request.param}")
    return request.param


#@pytest.fixture(autouse=True)
@pytest.fixture()
def run_before():
    print("Running before")


@pytest.fixture()
def run_before_and_after():
    print("before")
    yield
    print("after")


@pytest.fixture(scope="function")
def run_before_and_complex_after(request):
    print("before complex")

    def after1():
        print("after1")

    def after2():
        print("after2")

    request.addfinalizer(after1)
    request.addfinalizer(after2)


def sum_it(a, b):
    return a + b

def test_sum(run_before_and_after):
    assert sum_it(1, 2) == 3


@pytest.mark.usefixtures("run_before")
def test_another_sum():
    assert sum_it(1, 4) == 5


def test_complex_sum(run_before_and_complex_after):
    assert sum_it(1, 1) == 2

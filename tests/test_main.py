# type: ignore

from hello.main import add


def test_foo():
    assert add(1, 2) == 3

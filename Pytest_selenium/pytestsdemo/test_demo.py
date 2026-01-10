import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_demo1(self):
        print("I am executing the first method")

    def test_demo2(self):
        print("I am executing the second method")

    def test_demo3(self):
        print("I am executing the third method")

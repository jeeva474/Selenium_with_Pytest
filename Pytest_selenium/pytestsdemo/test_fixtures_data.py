import pytest


@pytest.mark.usefixtures("setup", "dataload")
class TestExample2:

    def test_datalaoding(self, dataload):
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])
        print(dataload[3])


@pytest.mark.usefixtures("crossbrowser")
class TestExample3:

    def test_executecrossbrowser(self, crossbrowser):
        print(crossbrowser)

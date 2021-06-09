import pytest

if __name__ == '__main__':
    pytest.main(["-m login ", r"--html=report\test.html", r"--alluredir=report\allure"])
    # pytest.main(["-m bid", r"--html=report\test.html"])

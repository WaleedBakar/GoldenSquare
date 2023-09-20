import pytest
from lib.password_checker import PasswordChecker

def test_if_password_is_valid():
    checker = PasswordChecker()
    checker.check = 8
    assert checker.check == 8

def test_if_password_is_invalid():
    checker = PasswordChecker()
    
    with pytest.raises(Exception) as e:
        checker.check("passw")
        message = str(e.value)
        assert message == "Invalid password, must be 8+ characters."



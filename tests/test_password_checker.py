import pytest
from lib.password_checker import PasswordChecker

def test_if_password_is_valid():
    checker = PasswordChecker()
    checker.len = 8
    assert checker.len == 8

def test_if_password_is_invalid():
    checker = PasswordChecker()
    
    with pytest.raises(Exception) as e:
        checker.wrap()
        message = str(e.value)
        assert message == "Invalid password, must be 8+ characters."



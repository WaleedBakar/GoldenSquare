import pytest
from lib.present import *

#when we wrap an item 
#we get it back when unwrapping


def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

# if we wrapp before wrapping we get an error message

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."
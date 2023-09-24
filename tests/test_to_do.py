from lib.to_do import check_for_todo

def test_check_for_todo():
    result = check_for_todo("This is a sample text with #TODO")
    assert result == True

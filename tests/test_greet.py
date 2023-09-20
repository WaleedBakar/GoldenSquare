from lib.greet import greet

def test_greet_person_of_name_given_name():
    result = greet('Kay')
    assert result == "Hello, Kay!"
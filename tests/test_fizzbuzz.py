from lib.fizzbuzz import fizzbuz


# Given a number not divisible by 3 or 5 (eg. 1)
# it returns that number

def test_given_non_3_5_divisible_returns_number():
    result = fizzbuz(1)
    assert result == 1


    #Given a number divisible by 3 it returns fizz

def test_given_3_divisible_returns_fizz():
    result = fizzbuz(9)
    assert result == "Fizz"

    # given a number divisible by 5 it returns 'buzz'

    def test_given_5_divisible_returns_buzz():
        result = fizzbuz(10)
        assert result == "Buzz"

# Given a number divisible by 3 and 5 it returns 'fizzbuzz'

def test_given_3_and_5_divisible_returns_fizzbuzz():
    result = fizzbuz(15)
    assert result == "Fizzbuzz"
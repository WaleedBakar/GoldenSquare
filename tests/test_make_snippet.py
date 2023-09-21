
from lib.make_snippet import make_snippet
# A function called 'make_snippet' that takes a string


# as an argument and returns the first five words and
# then a "..." if there are more than that.


def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""

# Given a string of four words it returns the same string

def test_given_four_word_string_returns_same_string():
    result = make_snippet("one two three four")
    assert result == "one two three four"

# given a string of 6 words it returns first 5 words and a ...

def test_given_6_words_returns_string_and_ellipsis():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."
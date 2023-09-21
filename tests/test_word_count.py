from lib.word_count import *
def test_count_words():
    
    result = count_words("Hello world")
    assert result == 2, f"Expected 2, but got {result}"

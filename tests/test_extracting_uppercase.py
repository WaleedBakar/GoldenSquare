from lib.extracting_uppercase import extract_uppercase



def test_extract_uppercase():
    mixed_words = "hello WORLD Example TEST"
    result = extract_uppercase(mixed_words)
    assert result == ["WORLD", "TEST"]


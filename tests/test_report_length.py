from lib.report_length import report_length

def test_length_of_report():
    result = report_length("Hello, World!")
    assert result == "This string was 13 characters long."
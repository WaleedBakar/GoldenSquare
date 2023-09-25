from lib.diary_entry import DiaryEntry

def test_count_words_in_both_title_and_contents():
    title = 'My Title'
    contents = "Some contents"
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.count_words()
    expected_result = 4  # The expected result is 4
    assert result == expected_result
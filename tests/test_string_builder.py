from lib.string_builder import StringBuilder

def test_building_a_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

from data_structures_and_algorithms401.challenges.multi_bracket_validation.multi_bracket_validation import *

def test_multi_bracket_validation_with_word():
    actual = multi_bracket_validation('{()[[any text]]}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_without_text():
    actual = multi_bracket_validation('{}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_without_text_two():
    actual = multi_bracket_validation('{({})}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_missing_curly_braces():
    actual = multi_bracket_validation('{({})')
    expected = False
    assert actual == expected

def test_multi_bracket_validation_with_extra_curly_braces():
    actual = multi_bracket_validation('{({})}}')
    expected = False
    assert actual == expected

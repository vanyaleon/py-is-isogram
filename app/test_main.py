from app.main import is_isogram


def test_is_isogram_is_empty_str():
    assert is_isogram("") is True


def test_is_not_isogram_if_repeat_upper_and_lower():
    assert is_isogram("Adam") is False


def test_is_it_isogram():
    assert is_isogram("Playgrounds ") is True


def test_not_only_non_consecutive_letters_are_not_an_isogram():
    assert is_isogram("look ") is False

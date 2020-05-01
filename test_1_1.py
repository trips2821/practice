import pytest

# Determine if a string has all unique characters
# Bonus, do it w/o additional data structures


def is_unique(string_to_test):
    char_reg = []
    for char in string_to_test:
        if char in char_reg:
            return False
        else:
            char_reg.append(char)

    return True


def test_unique_string():
    string = '1234567890'
    assert is_unique(string)


def test_not_unique_string():
    string = '12345678901'
    assert not is_unique(string)


def is_unique_no_extra_data_structs(string_to_test):
    string_length = len(string_to_test)

    for x in range(string_length):
        for y in range(string_length):
            if x == y: continue
            if string_to_test[x] == string_to_test[y]:
                return False

    return True


def test_is_unique_no_extra_data_structs_unique_string():
    string = '1234567890'
    assert is_unique_no_extra_data_structs(string)


def test_is_unique_no_extra_data_structs_not_unique_string():
    string = '12345678901'
    assert not is_unique_no_extra_data_structs(string)

import pytest

# Write a function to determine if 2 strings are permutations of one another

def set_are_similar(string1, string2):
    result =  not set(string1) - set(string2)
    return result

def test_similar_string():
    string1 = '1234567890'
    string2 = '0987654321'

    assert set_are_similar(string1, string2)

def test_dissimilar_string():
    string1 = '1234567890'
    string2 = '0987654329'

    assert not set_are_similar(string1, string2)

def n_are_similar(string1, string2):
    if len(string1) != len(string2):
        return False

    string1 = sorted(string1)
    string2 = sorted(string2)

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False


    return True

def test_n_similar_string():
    string1 = '1234567890'
    string2 = '0987654321'

    assert n_are_similar(string1, string2)

def test_n_similar_different_length_strings():
    string1 = '1234567890'
    string2 = '0987654321000'

    assert not n_are_similar(string1, string2)

def test_n_dissimilar_string():
    string1 = '1234567890'
    string2 = '0987654329'

    assert not n_are_similar(string1, string2)

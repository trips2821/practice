import pytest

# write a function to replace all spaces w/ %20.  Assume there is enough room at the end to hold entire string
# and that you are given the true length of the string

def url_encode(string):
    split_str = string.split()
    result = "%20".join(split_str)

    return result


def test_replace_characters():
    expected_value = "Mr%20John%20Smith"
    starting_value = "Mr John Smith    "
    true_length = 13

    assert url_encode(starting_value) == expected_value


def bytearray_url_encode(string, true_length):
    encoded_string = string.encode('UTF-8')
    ba = bytearray(encoded_string)

    array_offset = true_length - 1
    string_length = len(ba)
    write_prt = string_length - 1

    for i in range(true_length):
        read_ptr = array_offset - i
        if ba[read_ptr] == ord(' '):
            write_prt -= 2
            ba[write_prt+2] = ord('0')
            ba[write_prt+1] = ord('2')
            ba[write_prt] = ord('%')
        else:
            ba[write_prt] = ba[read_ptr]

        write_prt -= 1

    decoded_string = ba.decode()
    return decoded_string


def test_bytearray_url_encode():
    expected_value = "Mr%20John%20Smith"
    starting_value = "Mr John Smith    "
    true_length = 13

    assert bytearray_url_encode(starting_value, true_length) == expected_value

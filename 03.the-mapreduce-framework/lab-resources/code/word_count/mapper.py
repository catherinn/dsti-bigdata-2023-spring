import sys
import re


def write_kv_array(kv_array):
    for kv in kv_array:
        print(f'{kv["key"]}\t{kv["value"]}')


def text_to_words(text):
    key_values = []

    for line in text:
        for word in line.strip().split():
            word = re.sub(r'[^\w]', '', word).lower()
            # regular expression pattern that matches any character that is not a word character. and turns lowercase
            # \w represents word characters (letters, digits, and underscores), 
            key_values.append({'key': word, 'value': 1})

    return key_values


if __name__ == '__main__':
    write_kv_array(text_to_words(sys.stdin))
# is a connection to the program's standard input, which is often associated with reading data from the keyboard when running the script in a terminal. However, it can also 
# be used to read data from other sources when the script is part of a pipeline or when input is redirected from a file or another program.

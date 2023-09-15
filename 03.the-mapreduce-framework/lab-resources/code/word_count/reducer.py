import sys


def read_kv_array(text):
    key_values = []

    for line in text:
        key, value = line.split('\t')
        key_values.append({'key': key, 'value': value})
    # appending each key value pair as a dictionary to the list keeps the order, while only using dictionary wouldn't
    return key_values


def write_kv_dict(key_values):
    for k, v in key_values.items():
        print(f'{k}\t{v}')


def word_count(words):
    # input is key_values as a list of dictionaries with key value pairs (word, and count)
    key_values = {}

    for w in words:
        key_values[w['key']] = key_values.get(w['key'], 0) + int(w['value'])
        # list of unique words(keys), counted. key_values.get retrieves a value associated with a specific key. either the existing key is added the new count, or the new key is added with its value
    return key_values


if __name__ == '__main__':
    write_kv_dict(word_count(read_kv_array(sys.stdin)))

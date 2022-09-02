def is_anagram(first_string, second_string):
    a = first_string.lower()
    b = second_string.lower()

    if len(a) != len(b):
        return False
    else:
        for letter in a:
            if a.count(letter) != b.count(letter):
                return False
        return True


print(is_anagram('amor', 'roma'))
print(is_anagram('perda', 'pedra'))
print(is_anagram('pato', 'tapo'))
print(is_anagram('amores', 'ramones'))
print(is_anagram('', 'roma'))
print(is_anagram('AmOr', 'RoMa'))

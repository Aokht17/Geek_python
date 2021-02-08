def int_func(string):
    """
    Capitalizes each word in a given string
    :return: str
    """
    return string.title()


print(int_func('text for test'))


# Но если очень хочется вызывать функцию внутри функции, то:

def int_func_1(word):
    """
    Capitalizes a word
    :return: str
    """
    return word.capitalize()


def str_capit(s_string):
    """
    Uses int_func_1 function for strings (phrases)
    """
    for i in s_string.split(" "):
        print(int_func_1(i), end=' ')


str_capit('too many words')

""""""

myStr = """Q2. (50 points) Implement function wordcount() that takes a string, and
returns the frequency of each word as a dictionary.
Note:
1. You should ignore the uppercase and lowercase. For example, 'Unicode'
and 'unicode' are considered as the same word.
2. The punctuations and digits should NOT be counted. You only need to
consider these punctuations: (),.!?'/[]"""


def clean(words):
    clean_str = ""
    bad_chars = ["(", ")", ",", ".", "!", "?", "'", "/", "[", "]", "\""]
    for char in words:
        if char not in bad_chars:
            clean_str += char
    return clean_str


def isNumber(word):
    for char in word:
        if not char.isdigit():
            return False
    return True


def word_count(my_str):
    words = clean(my_str).lower().split(" ")
    my_dic = {}
    for word in words:
        if isNumber(word):
            pass
        else:
            if word in my_dic:
                my_dic[word] += 1
            else:
                my_dic[word] = 1

    return my_dic

def f(b):
    a=6
    return a*b

a=0
print('{}' .format(f(3)))
print('{}' .format(a))



print(word_count(myStr))
import re


def ispalindrome(word):
    forwards = ''.join(re.findall(r'[a-z]+', word.lower()))
    return forwards == forwards[::-1]

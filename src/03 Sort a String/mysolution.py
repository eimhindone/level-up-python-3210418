def sortstring(words):
    return ' '.join(sorted(words.split(), key=str.casefold))

"""
Uses reverse indexing to check the last value of the string - if "s" then the word is plural
"""
def is_plural(word):
    if word[-1] == "s":
        return True
    else:
        return False
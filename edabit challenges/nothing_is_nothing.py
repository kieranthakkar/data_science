"""
Given any number of parameters (which is signified using *args syntax), return True if none of the variables are falsy/empty.
"""
def nothing_is_nothing(*args):
    return all(args) != (None or False)
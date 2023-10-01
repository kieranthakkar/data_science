"""
Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.
"""
def test_jackpot(list):
    return list[0] == list[1] == list[2] == list[3]

print(test_jackpot(["@", "@", "@", "@"]))
print(test_jackpot(["abc", "abc", "abc", "abc"]))
print(test_jackpot(["SS", "SS", "SS", "SS"]))
print(test_jackpot(["&&", "&", "&&&", "&&&&"]))
print(test_jackpot(["SS", "SS", "SS", "Ss"]))
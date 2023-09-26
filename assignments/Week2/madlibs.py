"""Project Brief
Mad Libs Generator
1. User is prompted for a series of inputs. e.g., a singular noun, an adjective, etc.
2. Program takes the inputs and places them into a pre-made story template.
3. Print out the full story w/ inputs inserted. """

# VOCABULARY EXPLANATION
# Verbs =
# Adverbs =
# Nouns =
# Adjectives =


dictionary = {"adjective":"", "place":"", "name":""}

for index, key in enumerate(dictionary):
    dictionary[key] = input(f"Word for <{key}>: ")

print(dictionary)
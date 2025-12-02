#print the unique characters and count of unique characters

name = "vineetha"

def print_unique_characters_and_count(name):
    unique_chars_in_name = set()
    for char in name:
        unique_chars_in_name.add(char)
    print(f"Unique characters in {name} are {unique_chars_in_name} and the count is {len(unique_chars_in_name)}")

print_unique_characters_and_count(name)
"""
    This exercise includes escape sequences in print and string statements
    In Learn Python 3 the Hard Way, refer to page 34-35 for whole list of escape sequences
"""

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

carriage_cat = "I'm is going to replace I'm in the beginning of the sentence.\r123"
octal_cat = "\110\145\154\154\157\40\127\157\162\154\144\41"
vertical_cat = "Look at my vert! \v"
backspace_cat = "Back \b that booty up."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t *Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print(carriage_cat)
print(octal_cat)
print(vertical_cat)
print(backspace_cat)
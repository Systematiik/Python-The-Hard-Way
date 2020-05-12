#This function splits the sentence into words
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

#sorts the words in alphabetical order
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#pops the first word and prints it
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

#pops the last word and prints it
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

#takes the sentence, sorts them, and prints them out in alphabetical order
def sort_sentence(sentence):
    """Takes a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

#prints the first and last word before the words are sorted
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#prints the first and last word after the words are sorted
def print_first_and_last_sorted(sentence):
    """Sorts the first and last words of the sentence."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
#In terminal, type: python ex23.py UTF-8 strict
#You can also use UTF-16, UTF-32, however not big5
#This will open the languages file
#"Deebees", decode bytes, encode strings

import sys
script, input_encoding, error = sys.argv

#this main method is used to print the contents of the language file
#the if statement is used to check for whether a line is present or not
#calling the main function is recursively calling itself until parameters are satisfied
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

#this takes each line and separates each line by raw bytes and cooked
#raw meaning the bytes that python reads
#cooked meaning decoded into UTF-8
#prints each individual line
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

#opens the text file, "languages.txt" and encodes to utf-8
languages = open("languages.txt", encoding="utf-8")

#this runs the main method
main(languages, input_encoding, error)
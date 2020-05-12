# reading textfiles by user input
# open() opens file when in same directory
# read() reads file 

from sys import argv
# takes argument and puts under variable txt and function open, opens filename
filename = input("Give me a text file to read (.txt): ")
txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read()) # prints contents of file into terminal

txt.close() # closes file after reading 
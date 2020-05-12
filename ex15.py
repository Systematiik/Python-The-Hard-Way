#reading textfiles by passing args and user input
#open() opens file when in same directory
#read() reads file 

from sys import argv
script, filename = argv

#takes argument and puts under variable txt and function open, opens filename
txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read()) #prints contents of file into terminal

txt.close()

print("Type the filename again: ")
file_again = input("> ") #asks for the name of the file again

#sets the file_again as a parameter for the open function in the variable txt_again
txt_again = open(file_again) 

#reads and prints the file txt_again into terminal
print(txt_again.read())

txt_again.close()

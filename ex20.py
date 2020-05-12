from sys import argv
script, input_file = argv

#this function applies a variable f to print everything that f owns 
def print_all(f):
    print(f.read())

#the seek function sets the variable f to the very first byte
def rewind(f):
    f.seek(0)

#this function prints out one line from variable f
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

#this prints the file being opened
print("First let's print the whole file:\n"); print_all(current_file)

#this function points the file to the very first byte
#essentially setting it to the top of the file
print("Now let's rewind, kind of like a tape."); rewind(current_file)

print("\nLet's print three lines:\n")
current_line = 1; print_a_line(current_line, current_file)
current_line = current_line + 1; print_a_line(current_line, current_file)
current_line = current_line + 1; print_a_line(current_line, current_file)
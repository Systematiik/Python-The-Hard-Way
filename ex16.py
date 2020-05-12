from sys import argv

#asks for arguments
script, filename = argv

print(f"We're going to erase {filename}.")
print("If we don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

#hitting ctrl-c causes a keyboard interrupt which breaks the script
#hitting enter or return truncates the textfile that was entered as an argument
input("?")

print("Opening the file...")
#opens the arg filename
#w indicates that the file being opened can be written on
#Note: w only allows the user to only write to the file. Cannot read.
#r+ allows read and write
target = open(filename, 'r+')

print("Truncating the file. Goodbye!")
#truncating a file wipes the text clean
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#the function write(), writes in the variables that were made prior to this call into the file
#Semi colons allow more than one command to be put in one line
target.write("> ", line1); target.write("\n"); target.write("> ", line2) ;target.write("\n"); target.write("> ", line3)

#Python file method flush() flushes the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.
#Python automatically flushes the files when closing them. But you may want to flush the data before closing any file.
##https://www.tutorialspoint.com/python/file_flush.htm
target.flush()
target.seek(0) #Sets cursor to top of the file

print("\nThis is what is in the file now: \n")
new_file = target.read()
print(new_file)

print("\nAnd finally, we close it.")
target.close()
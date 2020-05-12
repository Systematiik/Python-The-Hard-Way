from sys import argv
from os.path import exists
#the module 'exists' is used to find whether a file exists or not by returning TRUE or FALSE

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file); indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.",
 f"\nDoes the output file exist? {exists(to_file)}.",
 "\nReady, hit RETURN to continue, CTRL-C to abort."
)
input("?")

out_file = open(to_file, 'w'); out_file.write(indata)

print("Alright, all done.")

#when a file is read it closes
#out_file isn't being read just written which means it should be closed when finished being used
out_file.close(); in_file.close()
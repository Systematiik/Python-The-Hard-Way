# Introduction to escape sequences such as end=

print("Mary had a little lamb")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) #multiplies the print of "." by 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#end= is a parameter within print that breaks a printline
#by default a print statement ends with a new line or "\n"

"""
    Ending the print statement with end= will allow the next print 
    statement to contine on the same line
    
    https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
"""

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
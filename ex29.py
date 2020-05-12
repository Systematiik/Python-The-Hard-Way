people = 20
cats = 30
dogs = 15

#20 < 30
#print
if people < cats:
    print("Too many cats! The world is doomed!")

#20 !> 30
#no print
if people > cats:
    print("Not many cats! The world is saved!")

#20 !< 15
#no print
if people < dogs:
    print("The world is drooled on!")

#20 > 15
#print 
if people > dogs:
    print("The world is dry!")

#dogs now equals 20
#dogs == people
#all statements below print
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
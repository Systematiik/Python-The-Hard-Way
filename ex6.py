types_of_people = 10
#the integer 10 is placed within the sentence
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

#the words "don't" and "binary" and put into this sentence
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
hilariousT = True
joke_eval = "Isn't that joke so funny?! {}"

#the ".format" allows the {} to have a value when putting in hilarious
print(joke_eval.format(hilariousT))

w = "This is the left side of ..."
e = " a string with a right side."

#These two sentences are concatanated to each other to become one sentence
print(w + e)
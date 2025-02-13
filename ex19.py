def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"\tYou have {cheese_count} cheeses!")
    print(f"\tYou have {boxes_of_crackers} boxes of crackers!")
    print("\tMan that's enough for a party!")
    print("\tGet a blanket.\n")

print("(1) We can just give the function numbers directly: ")
cheese_and_crackers(20,30)

print("(2) OR, we can use variables from our script: ")
amount_of_cheese = 10; amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("(3) We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 6)

print("(4) And we can combine the two, variables and math.")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
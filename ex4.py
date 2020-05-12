#represents how many cars we have
cars = 100

#number of seats available in car
space_in_a_car = 4

#number of drivers available
drivers = 30

#number of passengers
passengers = 90

#number of cars that were not driven
cars_not_driven = cars - drivers

#number of cars that are being driven
cars_driven = drivers

#number of available seats in total relative to the number of drivers
carpool_capacity = cars_driven * space_in_a_car

#average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
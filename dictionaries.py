car_details = {"car_make" : "Toyota",
               "car_model" : "Corolla"}
print(car_details)
make = car_details["car_make"]
car_details["year"] = 2024
print(car_details)
car_details["colour"] = "Red"
print(car_details)
del car_details["colour"]
print(car_details)
del car_details
#print(car_details) #Raises error as car_details 
                    #dictionary has been deleted

#For GPS coordinates, tuple as the values are fixed and ordered
#For shopping cart items, a list would work as it has full flexibility when it comes to changing items afterwards
#To find common values between lists, a set since you can apply union, intersect and difference operations on them
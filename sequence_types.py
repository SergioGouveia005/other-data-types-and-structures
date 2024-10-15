your_list = [13 + 2, "Text", 15, 23.4, "Programming"] #1
print(len(your_list)) #2
your_list.append("Hello") #3
your_list.insert(0, 99.9) #4
your_list.remove(your_list[-1]) #5
length = len(your_list) #6
print(your_list[0]) #7
your_list[1] = 15 + 2 #8
print(type(your_list)) #9
your_tuple = tuple(your_list) #10
print(type(your_tuple)) #11
print(your_tuple[0]) #12
print(len(your_tuple)) #13
#tuple[0] = 14 + 2 #*Errors out* #14
another_tuple = (123, "Hello", 12.3) #15
joined_tuple = your_tuple + another_tuple #16
print(another_tuple) #17
your_list = list(joined_tuple) #18
print(type(your_list)) #19
your_set = set(your_list) #20
print(len(your_set)) #21
your_set.add("Another item") #22
print(your_set) #23
your_set.add("Hello") #24
print(your_set) #25
another_set = {1,2,3,"Hello"} #26
new_set = your_set & another_set #27
print(new_set) #& creates a set with items common in both sets
               #your_set ∩ another_set 



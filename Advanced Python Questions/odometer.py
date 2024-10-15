def get_difference(actual_number):
    skipped_number = int(str(actual_number).replace("5", "6"))
    print(actual_number, "Actual")
    print(skipped_number, "Skipped")
    difference = skipped_number - actual_number
    return difference

apparent_distance = 160648
total_difference = 0
for i in range(apparent_distance):
    if str(i).__contains__("5"):
        total_difference += get_difference(i)

#print(total_difference)
print(abs(apparent_distance - total_difference))


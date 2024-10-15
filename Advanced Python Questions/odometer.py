apparent_distance = 160648
actual_distance = 0
for i in range(1, apparent_distance + 1):
    if str(i).__contains__("5"):
        i = int(str(i).replace("5", "6"))
        continue
    actual_distance += 1
    print(i, actual_distance)
print("The actual distance travelled is:", actual_distance)



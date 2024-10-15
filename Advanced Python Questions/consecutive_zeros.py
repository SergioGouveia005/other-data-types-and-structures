bin_str = input("Enter a binary string: ")
count = 0
longest_chain = 0

for i in range(len(bin_str)):
    if bin_str[i] == "0":
        count += 1
    else:
        if count > longest_chain:
            longest_chain = count
        count = 0

print("The length of the longest chain of zeros is:", longest_chain)
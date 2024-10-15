def format_rle(input_string):
    _list = []
    index = 0
    for i in input_string:
        if len(_list) == 0:
            _list.append(list(i))
        elif _list[index].__contains__(i):
            _list[index].append(i)
        else:
            _list.append(list(i))
            index += 1

    rle_string = ""
    for j in range(len(_list)):
        rle_string += f"{len(_list[j])}{_list[j][0]}"
    return rle_string

def format_rle_alternate(input_string):
    _list = []
    str = ""
    for i in range(len(input_string)):
        if i == 0:
            str += input_string[i]
        elif input_string[i] == input_string[i - 1]:
            str += input_string[i]
        else:
            _list.append(str)
            str = ""
            str += input_string[i]
    _list.append(str)

    rle_string = ""
    for i in range(len(_list)):
        rle_string += f"{len(_list[i])}{_list[i][0]}"
    return rle_string

input_string = (input("Enter a string of letters: ")).upper()
print(f"format_rle output: {format_rle(input_string)}")
print(f"format_rle_alternate output: {format_rle_alternate(input_string)}")



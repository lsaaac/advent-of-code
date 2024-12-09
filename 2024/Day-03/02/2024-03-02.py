# https://adventofcode.com/2024/day/3


def read_file(file_name):
    file_path = f"../{file_name}" 
    file_output = "" 

    with open(file_path) as file:
        file_output = ''.join(line.strip() for line in file)

    return file_output

def find_all_substrings(substring, string):
# Fin
    position = string.find(substring)
    position_output = []
    
    while position != -1:
        position_output.append(position)
        position = string.find(substring, position +1)

    return position_output

def find_is_int(tested_list, variable_index, potential_length):
# Finds whether a certain amount of consecutive variables are a certain type.
# deal w/ strings slicing out of index
    variable_length = 0
    variable_test = tested_list[variable_index : min(variable_index + potential_length, len(tested_list))]

    for variable in variable_test:
        if variable.isdigit():
            variable_length += 1
        else:
            break
    
    return variable_length
        

output = read_file("input.txt")
print(output)

counted = 0
uncounted = 0
valid_int_pairs = []
potential_string_information = {}
#for line in output:
# Find each segment in the mul(???,???) expected data format.
potential_string_starting_positions = []

#    print("Data")
#    print(line)

# Find "mul("
potential_string_starting_positions = find_all_substrings("mul(", output)

# Find integer 1
for starting_position in potential_string_starting_positions:
    do_position = output.rfind("do()", 0, starting_position)
    dont_position = output.rfind("don't()", 0, starting_position)


    if dont_position > do_position:
        counted += 1
        continue
    else:
        uncounted += 1
        pass

    valid_int_pair = []
    potential_string_dictionary = {"start": starting_position}

    potential_string_dictionary["length_int_1"] = find_is_int(output, starting_position + 4, 3) 

    potential_string_dictionary["comma_present"] = output[potential_string_dictionary["start"] + 4 
                                                        + potential_string_dictionary["length_int_1"]] == ","

    potential_string_dictionary["length_int_2"] = find_is_int(output, starting_position + 4 
                                                              + potential_string_dictionary["length_int_1"] + 1, 3)

    potential_string_dictionary["closing_bracket"] = output[potential_string_dictionary["start"] + 4 + potential_string_dictionary["length_int_1"] + 1 + potential_string_dictionary["length_int_2"]] == ")"


    check_ints = (potential_string_dictionary["length_int_1"] and potential_string_dictionary["length_int_2"]) > 0 
    check_strings = (potential_string_dictionary["comma_present"] and potential_string_dictionary["closing_bracket"]) == True

    valid_string = check_ints and check_strings

#        print(f"DO: {do_position}")
#        print(f"DONT: {dont_position}")

    if valid_string == True:
        print("VALID STRING")
        print(potential_string_dictionary, valid_string)
        print(f"check_ints: {check_ints}, check_strings: {check_strings}, valid_string: {valid_string}")
        print(output[int(potential_string_dictionary["start"]): int(potential_string_dictionary["start"])+12])
        int_1_start_position = potential_string_dictionary["start"] + 4
        int_2_start_position =  potential_string_dictionary["start"] + 4 +  potential_string_dictionary["length_int_1"] + 1

        valid_int_pair.append(int(output[int_1_start_position: int_1_start_position + potential_string_dictionary["length_int_1"]]))
        valid_int_pair.append(int(output[int_2_start_position: int_2_start_position + potential_string_dictionary["length_int_2"]]))

        valid_int_pairs.append(valid_int_pair)
        print(valid_int_pair)
    else:
        continue

#print("FINAL LIST")
#print(valid_int_pairs)

total = 0

for int_pair in valid_int_pairs:
    total += int_pair[0] * int_pair[1]

print(f"COUNTED: {counted} SKIPPED: {uncounted}")
print("TOTAL")
print(total)

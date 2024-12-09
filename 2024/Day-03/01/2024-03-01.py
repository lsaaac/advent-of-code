# https://adventofcode.com/2024/day/3



def read_file(file_name):
    file_path = f"../{file_name}" 
    file_output = []

    with open(file_path) as file:
        for line in file:
            file_output.append(line.strip())

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
        

output = list(read_file("input.txt"))

#print("FILE CONTENTS")
#for line in output:
#    print(line)
#print()
#
#print("FIND FUNCTION")
#print(output[0])
#substring_positions = find_all_substrings("mul(", output[0])
#print("mul(")
#print(substring_positions)
#for value in substring_positions:
#   print(output[0][value: value + 4], end = " ") 
#print()
#
#print("FIND INTS")
#int_positions_1 = []
#for potential_int in substring_positions:
#    int_positions_1.append(find_is_int(output[0], potential_int + 4, 3))
#print(int_positions_1)
#
#print("FIND SEPARATOR")
#separator_positions = []
#counter = 0
#for potential_separator in substring_positions:
#    if output[0][potential_separator + 4 + int_positions_1[counter]] == ",":
#        separator_positions.append(potential_separator + 4 + int_positions_1[counter])
#        counter += 1
#    else:
#       separator_positions.append("x")
#       counter += 1 
#print(separator_positions)
#
#print("FIND INTS AGAIN")
#int_positions_2 = []
#for potential_int in separator_positions:
#    int_positions_2.append(find_is_int(output[0], potential_int + 1, 3))
##print(int_positions_2)
#
#print("FIND END")
#end_positions = []
#counter = 0
#for potential_end in separator_positions:
#    #print(potential_end)
#    if output[0][potential_end + 1 + int_positions_2[counter]] == ")":
#        end_positions.append(potential_end + 1 + int_positions_2[counter])
#        counter += 1
#    else:
#       #separator_positions.append("x")
#       counter += 1 
#print(end_positions)


valid_int_pairs = []
potential_string_information = {}
for line in output:
# Find each segment in the mul(???,???) expected data format.
    potential_string_starting_positions = []

    print("Data")
    print(line)

    # Find "mul("
    potential_string_starting_positions = find_all_substrings("mul(", line)

    # Find integer 1
    for starting_position in potential_string_starting_positions:
        valid_int_pair = []
        potential_string_dictionary = {"start": starting_position}

        potential_string_dictionary["length_int_1"] = find_is_int(line, starting_position + 4, 3) 

        potential_string_dictionary["comma_present"] = line[potential_string_dictionary["start"] + 4 
                                                            + potential_string_dictionary["length_int_1"]] == ","

        potential_string_dictionary["length_int_2"] = find_is_int(line, starting_position + 4 
                                                                  + potential_string_dictionary["length_int_1"] + 1, 3)

        potential_string_dictionary["closing_bracket"] = line[potential_string_dictionary["start"] + 4 + potential_string_dictionary["length_int_1"] + 1 + potential_string_dictionary["length_int_2"]] == ")"


        check_ints = (potential_string_dictionary["length_int_1"] and potential_string_dictionary["length_int_2"]) > 0 
        check_strings = potential_string_dictionary["comma_present"] and potential_string_dictionary["closing_bracket"] == True

        valid_string = check_ints and check_strings

        print(potential_string_dictionary, valid_string)

        if valid_string:
            int_1_start_position = potential_string_dictionary["start"] + 4
            int_2_start_position =  potential_string_dictionary["start"] + 4 +  potential_string_dictionary["length_int_1"] + 1

            valid_int_pair.append(int(line[int_1_start_position: int_1_start_position + potential_string_dictionary["length_int_1"]]))
            valid_int_pair.append(int(line[int_2_start_position: int_2_start_position + potential_string_dictionary["length_int_2"]]))

            valid_int_pairs.append(valid_int_pair)

print("FINAL LIST")
print(valid_int_pairs)

total = 0

for int_pair in valid_int_pairs:
    total += int_pair[0] * int_pair[1]

print("TOTAL")
print(total)


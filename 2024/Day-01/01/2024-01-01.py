# https://adventofcode.com/2024/day/1

list_input_1 = []
list_input_2 = []
list_result = []

line = ""
result = 0 


# Read the file line by line, splitting each line into two numbers and appending
# them to seperate lists.
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        list_input_1.append(int(line[0]))
        list_input_2.append(int(line[1]))
        
list_input_1.sort()
list_input_2.sort()

# Find the distance between corresponding values in the two input lists and 
# populate a third list with those distances.`
for number in range(0 , len(list_input_1)):
    list_result.append(abs((list_input_1[number] - list_input_2[number])))

result = sum(list_result)

print(f"Total distance: {result}")

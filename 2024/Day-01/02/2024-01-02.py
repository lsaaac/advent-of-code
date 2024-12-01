# https://adventofcode.com/2024/day/1#part2

list_input_1 = []
list_input_2 = []

line = ""
result = 0 


# Read the file line by line, splitting each line into two numbers and appending
# them to seperate lists.
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        list_input_1.append(int(line[0]))
        list_input_2.append(int(line[1]))

# Find the number of times each value in the first array is found in the second.
# Multiply the value by the frequency of its occurance in the second list and 
# add that number to a counter.
for number in range(0 , len(list_input_1)):
    result += list_input_1[number] * list_input_2.count(list_input_1[number])

print(f"Similarity Score: {result}")

# Write a method to replace all spaces in a string with '%20' - URLify
input = "Mr John Smith    "
in_list = list(input)
length = 13

# Use two indices to move at different speed
slow_ind = len(input)-1

for i in range(length-1,-1, -1):
    if ord(in_list[i]) != ord(' '):
        in_list[slow_ind] = in_list[i]
        slow_ind -= 1
    else:
        in_list[slow_ind] = '0'
        in_list[slow_ind-1] = '2'
        in_list[slow_ind-2] = '%'
        slow_ind -= 3

output = "".join(in_list)
print(output)



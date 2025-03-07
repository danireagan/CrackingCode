# Given two strings, identify if it is a permutation of the palindrome
input_str = input("Enter the string")
input_str = input_str.lower()

# Using a dictionary to track the count of characters. - O(N)
char_list = {}

for ch in input_str:
    if ch == ' ':
        continue
    if char_list.get(ch,0) == 0:
        char_list[ch] = char_list.get(ch,0) + 1
    else:
        char_list.pop(ch)

print(char_list)
count = 0
for items in char_list.values():
    count += items
    # print(count)

if count < 2:
    print("Palindrome Permutation")
else:
    print("Not a palindrome")
    



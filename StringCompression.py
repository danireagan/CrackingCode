# Basic String compression using count of repeated characters

string1 = input("Enter the string") 

charToCount = string1[0]
count = 0
result = []

for ind in range(len(string1)):
    if charToCount == string1[ind]:
        count += 1
    else:
        result.append(charToCount)   
        result.append(str(count))
        count = 1
        charToCount = string1[ind]

result.append(charToCount)
result.append(str(count))

if len(result) < len(string1):
    output = "".join(result)
else:
    output = string1

print(output)
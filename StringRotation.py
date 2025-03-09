# String Rotation - given two strings, find one is rotated version of another

String1 = input("Enter string 1")
String2 = input("Enter string 2")

if len(String1) != len(String2):
    print("Not a rotated version")

ind1 = 0
ind2 = 0
while ind1 < len(String1):
    if String1[ind1] == String2[ind2]:
        ind2 += 1
    ind1 += 1

subString = String2[ind2:]
print(subString)

if subString in String1:
    print("String2 is a rotated version")
else:
    print("Not a rotated version")

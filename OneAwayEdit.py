# Find if two strings are one edit away

string1 = input("Enter string 1")
string2 = input("Enter string 2")

def OneReplace(string1, string2):
    AlreadyDiffer = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if AlreadyDiffer:
                return False
            AlreadyDiffer = 1
    return True

def OneEdit(string1, string2):
    ind1=0
    for ind2 in range(len(string2)):
        if string1[ind1] != string2[ind2]:
            ind1 += 1
            if ind1 - ind2 > 1:
                return False
        ind1 += 1
    return True

if len(string1) == len(string2):
    res = OneReplace(string1, string2)
elif len(string1) == len(string2) + 1:
    res = OneEdit(string1, string2)
elif len(string1) + 1 == len(string2):
    res = OneEdit(string2,string1)
else:
    res = False

print(res)
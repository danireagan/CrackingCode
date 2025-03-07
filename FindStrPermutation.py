# Given two strings, identify if one is the permutation of other string

InputWord1 = input("Enter String 1")
InputWord2 = input("Enter String 2")

# Method 1 - sort the strings and identify if they have the same list of characters - Complexity O(N log N)

word1 = sorted(InputWord1)
word2 = sorted(InputWord2)

if len(word1) != len(word2):
    print("1")
    print("Not a permutation")

flag = 0
for i in range(len(word1)):
    if word1[i] != word2[i]:
        flag = 1
        break

if flag == 1:
    print("Not a permutation")
else:
    print("permutation match")

#Method 2 - Using an array to count the characters - O(N)
hashTable = [0] * 26

lowerWord1 = InputWord1.lower()
lowerWord2 = InputWord2.lower()
for ch in lowerWord1:
    ind = ord(ch) - ord('a')
    hashTable[ind] = hashTable[ind] + 1
# print(hashTable)
for ch in lowerWord2:
    ind = ord(ch) - ord('a')
    hashTable[ind] -= 1

res = sum(hashTable)

# print(hashTable, res)

if res == 0:
    print("HashTable Permutation Match")
else:
    print("HashTable Not match")

hashDict = {}
for ch in InputWord1:
    hashDict[ch] = hashDict.get(ch,0) + 1

for ch in InputWord2:
    hashDict[ch] = hashDict.get(ch,0) - 1

# print(hashDict.values())
# res = sum(hashDict.values())
flag = 0
for items in hashDict.values():
    if items != 0:
        flag = 1
        break

if flag == 0:
    print("HashTable Permutation Match")
else:
    print("HashTable Not match")



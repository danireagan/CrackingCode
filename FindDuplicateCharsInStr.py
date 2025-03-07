# Implement an algorithm to find if a string contains duplicate elements.
# Method 1 - Using set to identify duplicates - Similar to hash table approach 
word=input("Enter the word")

unique = set(word.lower())
word = word.lower()

if len(word) == len(unique):
    print("Unique characters")
else:
    print("Repeated characters")

# Method 2 - Using bit vector to identify duplicates
def findDuplicate(s):
    bitVector = 0
    duplicates = set()
    for ch in s:
        bitPosition = ord(ch) - ord('a')
        bitMask = 1 << bitPosition

        if bitMask & bitVector:
            duplicates.add(ch)
        else:
            bitVector |= bitMask
    
    return duplicates

dups = findDuplicate(word)

print(dups)

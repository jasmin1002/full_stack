# Check if two words are anagrams
def find_anagrams(subject="", anagram=""):
    index = 0
    isAnagram = False

    # Return 'False' for empty string (i.e empty is not considered a word)
    if (len(subject) == 0 or len(anagram) == 0):
        return False

    # Pass letters and numeric characters.
    # Avoid repetition of letter and numeric characters.
    # And turns uppercase letter to lowercase if need be.
    subject = ''.join(filter(lambda x:x.isalpha() or x.isdigit(), sorted(set(subject.lower()))))
    anagram = ''.join(filter(lambda x:x.isalpha() or x.isdigit(), sorted(set(anagram.lower()))))

    # Set isAnagram 'False' if either sets are not the same
    # Otherwise 'True'
    while (index < len(subject)):
        if (subject[index].lower() != anagram[index].lower()):
            isAnagram = False
            break
        else:
            isAnagram = True
        
        index += 1

    # Return False or True depending on evaluation in while block
    return isAnagram

result = find_anagrams("hello", "check")
print(result)
print('-----------------------------------')

result = find_anagrams("below", "elbow")
print(result)
print('------------------------------------')

result = find_anagrams("ccccc", "c")
print(result)


# result = find_anagrams("Heavy rain", "Hire a Navy")
# print(result)
# print("-------------------------------------------")
# result = find_anagrams(
#     "To be or not to be: that is the question, whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune.",
#     "In one of the Bard's best-thought-of tragedies, our insistent hero, Hamlet, queries on two fronts about how life turns rotten."
# )
# print(result)
# print ("------------------------------------------")

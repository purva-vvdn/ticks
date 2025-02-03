def count_occurrence(str1):
    dict1 = {}
    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    return dict1

# Input from the user
str1 = input("Enter String: ")

# Count occurrences of each character
dict2 = count_occurrence(str1)

# Sort the dictionary by keys (characters)
sorted_by_keys = dict(sorted(dict2.items()))

# Sort the dictionary by values (occurrences)
sorted_by_values = dict(sorted(dict2.items(), key=lambda item: item[1]))


print("Original Dictionary:", dict2)
print("Sorted Dictionary by Keys:", sorted_by_keys)
print("Sorted Dictionary by Values:", sorted_by_values)

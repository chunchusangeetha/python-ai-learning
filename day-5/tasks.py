# group anargams

list_of_words = ["eat", "tea", "tan", "ate", "nat", "bat","tab","ten"]
anagram_map = {}

for ele in list_of_words:
    sorted_word = "".join(sorted(ele))
    if sorted_word in anagram_map:
        anagram_map[sorted_word].append(ele)
    else:
        anagram_map[sorted_word] = [ele]

print(list(anagram_map.values()))
  
# First Non-Repeating Character

def uni_char(name):
    first_uni_char = {}
    for char in name:
        if char not in  first_uni_char:
            first_uni_char[char] = 1
        else:
            first_uni_char[char] += 1 
    
    for char in first_uni_char:
        if first_uni_char[char] == 1:
            return char
    return None

print(uni_char("sageseatha"))
        
# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined = dict1 | dict2
print(combined)     

#Longest Word in List
fruits = ["apple", "banana", "kiwiuuuu"]

fruits_dict = {}
for fruit in fruits:
    fruits_dict[fruit] = len(fruit)

longest_word = ""
max_length = 0

for fruit,length in fruits_dict.items():
    if length > max_length:
        max_length = length
        longest_word = fruit
print(longest_word)   
    
longest_word = max(fruits, key=len)
print(longest_word)    
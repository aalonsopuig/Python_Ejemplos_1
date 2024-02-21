# This program showcases common list operations in Python, illustrating how to manipulate lists.
# Operations demonstrated include appending elements, inserting elements at specific positions,
# sorting the list, removing elements by value, popping elements by index, reversing the list,
# counting occurrences of an element, and finding an element's index. 


# Define a list of strings
fruits = ["apple", "banana", "apple", "cherry"]

# Append an item to the list
fruits.append("orange")
print ("a) ",fruits)

# Insert an item at a specific index
fruits.insert(1, "blueberry")  # Insert "blueberry" at index 1
print ("b) ",fruits)

# Sort the list in alphabetical order
fruits.sort()
print ("c) ",fruits)

# Removing an element by value
fruits.remove("banana")
print ("d) ",fruits)

# Pop an element by index (remove and return the last element if no index is specified)
last_fruit = fruits.pop()
print ("e) ",fruits)

# Reverse the list
fruits.reverse()
print ("f) ",fruits)

# Get the number of occurrences of an element
count_apple = fruits.count("apple")

# Find the index of an element
index_of_cherry = fruits.index("cherry")

print("Modified list:", fruits)
print("Last fruit removed:", last_fruit)
print("Count of 'apple':", count_apple)
print("Index of 'cherry':", index_of_cherry)

# list_warmup.py

# Create a list with four fruits
fruits = ["apple", "banana", "mango", "orange"]

# Print the first and last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Append a fifth fruit and print the whole list
fruits.append("strawberry")
print("After adding a fruit:", fruits)

# Remove one fruit and print the updated list
fruits.remove("banana")
print("After removing a fruit:", fruits)

# Print the number of remaining fruits
print("Total fruits remaining:", len(fruits))

# Create an empty dictionary
animal = dict()
# Add k/v pairs
animal["name"] = "Kevin"
animal["breed"] = "Bulldog"
animal["age"] = 5

# Create the dictionary with k/v pairs and assign to variable
animal = {
    "name": "Kevin",
    "breed": "Bulldog",
    "age": 5
}


for (key, value) in animal.items():
    print(f"{key}: {value}")

# Output
#name: Kevin
#breed: Bulldog
#age: 5


word_definitions = dict()

word_definitions["cool"] = "the man"
word_definitions["sweet"] = "I like it"
word_definitions["gnarley"] = "awesome"
word_definitions["bad"] = "good"

print(word_definitions)

print(word_definitions["cool"])
print(word_definitions['sweet'])


for word, definition in word_definitions.items():
    print(f"the definition of {word} is {definition}")
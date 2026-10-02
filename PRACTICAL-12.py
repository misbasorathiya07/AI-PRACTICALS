# Text Processing Program in Python

text = input("Enter a text: ")

# Convert text to lowercase
lower_text = text.lower()

# Convert text to uppercase
upper_text = text.upper()

# Count words
words = text.split()
word_count = len(words)

# Count characters
character_count = len(text)

# Count sentences
sentence_count = text.count(".") + text.count("?") + text.count("!")

# Display results
print("\n--- Text Processing Result ---")
print("Lowercase:", lower_text)
print("Uppercase:", upper_text)
print("Number of words:", word_count)
print("Number of characters:", character_count)
print("Number of sentences:", sentence_count)
from collections import defaultdict, Counter

# Training text
text = """
I love python programming.
I love machine learning.
Machine learning is interesting.
Python programming is easy.
"""

# Convert text into words
words = text.lower().replace(".", "").split()

# Create Bigram model
bigram = defaultdict(Counter)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    bigram[current_word][next_word] += 1

# Function to predict next word
def predict_next_word(word):
    word = word.lower()

    if word in bigram:
        return bigram[word].most_common(1)[0][0]
    else:
        return "No prediction available"

# User input
word = input("Enter a word: ")

# Prediction
prediction = predict_next_word(word)

print("Predicted next word:", prediction)
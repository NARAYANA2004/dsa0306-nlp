import re

# Define the text to be tagged
text = "I bought a new laptop yesterday"

# Define regular expression patterns for different POS tags
patterns = [
    (r'\b[A-Z][a-z]*\b', 'Noun'),  # Words starting with a capital letter
    (r'\b[a-z]*ly\b', 'Adverb'),   # Adverbs ending in 'ly'
    (r'\b[a-z]*ed\b', 'Verb'),     # Past tense verbs ending in 'ed'
    (r'\b[a-z]*ing\b', 'Verb'),    # Present participle verbs ending in 'ing'
    (r'\b[a-z]*ous\b', 'Adjective')# Adjectives ending in 'ous'
]

# Initialize an empty list to store the tagged text
tagged_text = []

# Assign POS tags based on the regular expression patterns
for word in text.split():
    tagged = False
    for pattern, tag in patterns:
        if re.match(pattern, word):
            tagged_text.append((word, tag))
            tagged = True
            break
    if not tagged:
        tagged_text.append((word, 'Noun'))  # Default to Noun if no pattern matches

# Print the tagged text
for word, tag in tagged_text:
    print(word, tag)

import random

# Define the probabilistic model (transition probabilities)
probabilistic_model = {
    'Noun': {'Noun': 0.3, 'Verb': 0.2, 'Adjective': 0.1, 'Adverb': 0.1},
    'Verb': {'Noun': 0.2, 'Verb': 0.3, 'Adjective': 0.1, 'Adverb': 0.1},
    'Adjective': {'Noun': 0.1, 'Verb': 0.1, 'Adjective': 0.3, 'Adverb': 0.2},
    'Adverb': {'Noun': 0.1, 'Verb': 0.1, 'Adjective': 0.2, 'Adverb': 0.3}
}

# Define the list of POS tags
pos_tags = ['Noun', 'Verb', 'Adjective', 'Adverb']

# Define the text to be tagged
text = "I bought a new laptop yesterday"

# Initialize an empty list to store the tagged text
tagged_text = []

# Assign POS tags to each word in the text based on the probabilistic model
for word in text.split():
    if not tagged_text:
        # Assign the first word a random POS tag
        tagged_text.append((word, random.choice(pos_tags)))
    else:
        # Assign POS tags based on transition probabilities
        prev_tag = tagged_text[-1][1]
        next_tag = random.choices(list(probabilistic_model[prev_tag].keys()), 
                                  weights=list(probabilistic_model[prev_tag].values()))[0]
        tagged_text.append((word, next_tag))

# Print the tagged text
for word, tag in tagged_text:
    print(word, tag)

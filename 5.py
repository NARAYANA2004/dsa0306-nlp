from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# List of words to perform stemming on
words = ["running", "easily", "friendship", "beautifully"]

# Initialize the Porter Stemmer
porter = PorterStemmer()

# Perform stemming on the list of words
stemmed_words = [porter.stem(word) for word in words]

# Display the stemmed words
for original, stemmed in zip(words, stemmed_words):
    print(f"Original: {original} -> Stemmed: {stemmed}")

import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet

# Sample text for morphological analysis
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
words = word_tokenize(text)

# Perform morphological analysis using WordNet in NLTK
for word in words:
    synsets = wordnet.synsets(word)
    if synsets:
        print(f"Word: {word}")
        for synset in synsets:
            print(f"Lemma: {synset.lemmas()[0].name()}")
            print(f"POS Tag: {synset.pos()}")
            print(f"Definition: {synset.definition()}")
        print("--------------------")

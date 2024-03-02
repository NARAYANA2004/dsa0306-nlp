import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download the NLTK data for tokenization and part-of-speech tagging
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    pos_tags = pos_tag(words)
    
    return pos_tags

# Example Usage
text = "NLTK is a powerful library for natural language processing."
pos_tags = pos_tagging(text)

print("Original Text:")
print(text)
print("\nPart-of-Speech Tags:")
print(pos_tags)

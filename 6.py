import random

def create_bigram_model(text):
    words = text.split()
    bigram_model = {}
    
    for i in range(len(words)-1):
        current_word = words[i]
        next_word = words[i+1]
        
        if current_word not in bigram_model:
            bigram_model[current_word] = []
        bigram_model[current_word].append(next_word)
    
    return bigram_model

def generate_text(bigram_model, starting_word, length=10):
    current_word = starting_word
    generated_text = [current_word]
    
    for _ in range(length-1):
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break
    
    return ' '.join(generated_text)

# Example Usage
text_corpus = "This is a simple example of a bigram model for text generation. You can modify the input text as needed."
bigram_model = create_bigram_model(text_corpus)

starting_word = "This"
generated_text = generate_text(bigram_model, starting_word, length=15)

print("Generated Text:")
print(generated_text)

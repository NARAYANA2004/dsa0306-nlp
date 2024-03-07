import spacy

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text
    doc = nlp(text)
    
    # Extract named entities
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    
    return entities

if _name_ == "_main_":
    # Example text
    text = """
    Apple Inc. is an American multinational technology company headquartered in Cupertino, California. 
    It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976 and is known for its innovative 
    products such as the iPhone, iPad, and MacBook.
    """
    
    # Perform NER
    entities = perform_ner(text)
    
    # Print named entities and their labels
    for entity, label in entities:
        print(f"Entity: {entity}, Label: {label}")

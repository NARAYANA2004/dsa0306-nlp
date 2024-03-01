# Finite-state machine for generating plural forms of English nouns without using a function

# Singular nouns to be pluralized
nouns = ["cat", "dog", "city", "box"]

# Apply rules to generate plural forms
plurals = []
for noun in nouns:
    plural = noun
    if noun.endswith('y'):
        plural = noun[:-1] + 'ies'
    elif noun[-1] in ['s', 'x', 'z'] or noun[-2:] in ['ch', 'sh']:
        plural = noun + 'es'
    else:
        plural = noun + 's'
    
    plurals.append(plural)

# Display the generated plural forms
for singular, plural in zip(nouns, plurals):
    print(f"Singular: {singular} -> Plural: {plural}")

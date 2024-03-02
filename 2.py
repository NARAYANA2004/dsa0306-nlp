def fsa(input_string):
    state = 0
    for char in input_string:
        if state == 0 and char == 'a':
            state = 1
        elif state == 1 and char == 'b':
            state = 2
        else:
            state = 0
    
    return state == 2

# Test the automaton with sample strings
print(fsa("cab"))  # False
print(fsa("abcab"))  # True
print(fsa("abab"))  # True

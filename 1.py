import re

# Sample text to search for patterns
text = "Hello, my email is example@email.com and my phone number is 123-456-7890."

# Define the pattern to search for an email address
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define the pattern to search for a phone number
phone_pattern = r'\d{3}-\d{3}-\d{4}'

# Search for the email address in the text
email = re.search(email_pattern, text)
if email:
    print("Email found:", email.group())

# Search for the phone number in the text
phone = re.search(phone_pattern, text)
if phone:
    print("Phone number found:", phone.group())

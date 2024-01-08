import re

# Sample text
text = "The quick brown fox jumps over the lazy dog."

# Define the pattern to search for
pattern = "fox"

# Use the search() method to find the first occurrence of the pattern in the text
match = re.search(pattern, text)

# Check if the pattern was found
if match:
    print(f"Pattern found: {match.group()}")
else:
    print("Pattern not found.")
    

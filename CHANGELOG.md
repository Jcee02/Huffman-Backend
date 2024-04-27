(2024-04-27)

# Fixes and improvements:

- **Added util functions to <huffman>.py including:**
    
 ```python
def generate_dict(filepath) -> dict:
    with open(filepath, 'r') as file:
        text = file.read()

    #Generate char occurrence list and cast it to dict
    enum_dict = dict(Counter(text).most_common())
    
    return enum_dict 
 ```
 * enum_dict was implicitly defined at main window function.

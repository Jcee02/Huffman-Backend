from collections import Counter

#Subroutines for main.py

def generate_dict(filepath) -> dict:
    with open(filepath, 'r') as file:
        text = file.read()

    #Generate char occurrence list and cast it to dict
    enum_dict = dict(Counter(text).most_common())
    

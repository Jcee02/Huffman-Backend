from collections import Counter

DICTIONARY_SIZE = 256
# Subroutines for main.py


# Wrapper for generate_dict for Tree construction instances
# Decorating generate_dict function extracts ordered frequency of given chars
def freq_decorator(dict):
    def wrapper():
        dummy_dict = dict
        freq = list(dummy_dict.values())
        print("Extracting ordered frequency list from Huffman dictionary")
        return freq
    return wrapper


def generate_dict(filepath) -> dict:
    with open(filepath, 'r') as file:
        text = file.read()

    # Generate char occurrence list and cast it to dict
    enum_dict = dict(Counter(text).most_common())
    return enum_dict




# Tree related:


class NodeTree(object):

    def __init__(self, right=None, left=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binString=''):
    # size of binString should be more than 1 for it to be str
    if type(node) is str:
        return {node: binString}

    (l, r) = node.children()
    d = dict()

    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

def compress(input):
    global DICTIONARY_SIZE
    dictionary = {}
    result = []
    temp = ""

    for i in range(0, DICTIONARY_SIZE):
        dictionary[str(chr(i))] = i

    for c in input:
        temp2 = temp+str(chr(c))
        if temp2 in dictionary.keys():
            temp = temp2
        else:
            result.append(dictionary[temp])
            dictionary[temp2] = DICTIONARY_SIZE
            DICTIONARY_SIZE += 1
            temp = ""+str(chr(c))


    if temp != "":
        result.append(dictionary[temp])  
        
    return result


def decompress(input):
    global DICTIONARY_SIZE
    dictionary = {}
    result = []

    for i in range(0, DICTIONARY_SIZE):
        dictionary[i] = str(chr(i))

    previous = chr(input[0])
    input = input[1:]
    result.append(previous)

    for bit in input:
        aux = ""
        if bit in dictionary.keys():
            aux = dictionary[bit]
        else:
            aux = previous+previous[0] 
            #Bit is not in the dictionary
                 # Get the last character printed + the first position of the last character printed
                 #because we must decode bits that are not present in the dictionary, so we have to guess what it represents, for example:
                 #let's say bit 37768 is not in the dictionary, so we get the last character printed, for example it was 'uh'
                 #and we take it 'uh' plus its first position 'u', resulting in 'uhu', which is the representation of bit 37768
                 #the only case where this can happen is if the substring starts and ends with the same character ("uhuhu").
        result.append(aux)
        dictionary[DICTIONARY_SIZE] = previous + aux[0]
        DICTIONARY_SIZE+= 1
        previous = aux
    return result

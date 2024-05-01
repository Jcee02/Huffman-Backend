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
 
(2024-04-30)

- **Decorated generate_dict to generate a list of frequencies:**

 ```python
def freq_decorator(dict):
    def wrapper():
        dummy_dict = dict
        freq = list(dummy_dict.values())
        print("Extracting ordered frequency list from Huffman dictionary")
        return freq
    return wrapper
 ```

 * freq list tought to be useful to enumerate node tuples for Huffman code 

 ```python
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

```

  * Implemented Huffman compression and decompression algorithms.
  * Added `NodeTree` class to represent nodes in the Huffman tree.
  * Added `huffman_code_tree` function to generate Huffman codes for characters based on the tree structure.
  * Introduced `compress` function to compress input data using Huffman coding.
  * Introduced `decompress` function to decompress Huffman-encoded data.
  * Added global constant `DICTIONARY_SIZE` to manage the size of the dictionary used in compression and decompression.



  * Refactored `compress` and `decompress` functions to improve readability and maintainability.
  * Updated comments and docstrings for better clarity and understanding.
  * Improved error handling and edge case management in compression and decompression algorithms.


  * Fixed a bug where incorrect characters were generated during decompression for certain inputs. (stack trash values)
  * Fixed potential issues related to global state management and dictionary size updates.


## Changes in the Final File compared to the Original

### Added
- Imported the `pickle` module for data serialization.
- Added the import statement for the `src.huffman` module to utilize functions related to file compression and decompression using the Huffman algorithm.
- New functions (`huff_txt`, `compress_txt`, `decompress_bin`) were added to perform file compression and decompression operations.

### Changed
- Modified the `ventana_bienvenida` function to incorporate new functionality for file compression and decompression.
- Refactored the `Abrir_Archivo` function to be more versatile and handle different file types for compression and decompression operations.
- Revised the structure of the GUI window to accommodate the new features for file compression and decompression.

### Removed
- Removed the import statement for the `collections` module as it was not utilized in the final file.
- Eliminated the `ventana_archivo_abierto` function from the original file as its functionality was integrated into the `huff_txt` function in the final file.

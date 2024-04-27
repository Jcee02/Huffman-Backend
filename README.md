# Huffman Algorithm.

## Project Description

Compressing algorithm for Algorithm Analysis course at Universidad de Guadalajara (CUCEI)



The following conventions are considered for the making of this project:

1. **Use of package relative imports:** to run a specific module consider:
    * python -m Huffman_Algorithm.src.<file>.py

2. **Binary encoding:** To represent a Huffman string (binary sequence) multiple Data Structures were explored, however, a Tree was chosen for utility means (traversal algorithms), once Huffman Tree is traversed (with each node containing the number of ocurrences for each char detected in the file handled), a binary ASCII hex format string is stored.

3. **Binary decoding:** Huffman codes were really useful when decoding the binary streams of data, so not much description is needed at the moment, note implementation details at src


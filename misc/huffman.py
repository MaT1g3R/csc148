"""
Code for compressing and decompressing using Huffman compression.
"""

from nodes import HuffmanNode, ReadNode


# ====================
# Helper functions for manipulating bytes


def get_bit(byte, bit_num):
    """ Return bit number bit_num from right in byte.

    @param int byte: a given byte
    @param int bit_num: a specific bit number within the byte
    @rtype: int

    >>> get_bit(0b00000101, 2)
    1
    >>> get_bit(0b00000101, 1)
    0
    """
    return (byte & (1 << bit_num)) >> bit_num


def byte_to_bits(byte):
    """ Return the representation of a byte as a string of bits.

    @param int byte: a given byte
    @rtype: str

    >>> byte_to_bits(14)
    '00001110'
    """
    return "".join([str(get_bit(byte, bit_num))
                    for bit_num in range(7, -1, -1)])


def bits_to_byte(bits):
    """ Return int represented by bits, padded on right.

    @param str bits: a string representation of some bits
    @rtype: int

    >>> bits_to_byte("00000101")
    5
    >>> bits_to_byte("101") == 0b10100000
    True
    """
    return sum([int(bits[pos]) << (7 - pos)
                for pos in range(len(bits))])


# ====================
# Functions for compression


def make_freq_dict(text):
    """ Return a dictionary that maps each byte in text to its frequency.

    @param bytes text: a bytes object
    @rtype: dict{int,int}

    >>> d = make_freq_dict(bytes([65, 66, 67, 66]))
    >>> d == {65: 1, 66: 2, 67: 1}
    True
    """
    out = {}
    for i in text:
        if i not in out:
            out[i] = 1
        else:
            out[i] += 1
    return out


def huffman_tree(freq_dict):
    """ Return the root HuffmanNode of a Huffman tree corresponding
    to frequency dictionary freq_dict.

    @param dict(int,int) freq_dict: a frequency dictionary
    @rtype: HuffmanNode

    The rule: at each step, merge the two smallest - frequency tree

    >>> freq = {2: 6, 3: 4}
    >>> t = huffman_tree(freq)
    >>> result1 = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> result2 = HuffmanNode(None, HuffmanNode(2), HuffmanNode(3))
    >>> t == result1 or t == result2
    True
    >>> freq = {1: 5, 2: 7, 3: 10, 4: 15, 5: 20, 6: 45}
    """
    def create_tree(new_node, prev_node):
        """Return a new HuffmanNode with root of None, number of total freq
        with left and right of respective node.

        Helper function!

        @param HuffmanNode new_node: a HuffmanNode
        @param HuffmanNode prev_node: another HuffmanNode
        @rtype: HuffmanNode
        """
        if new_node is not None and prev_node is not None:
            tree = HuffmanNode(None, new_node, prev_node)
            tree.number = new_node.number + prev_node.number
            return tree
        else:
            return HuffmanNode(None)

    def build_tree(symbol, number):
        """Build a HuffmanNode from the given symbol and number.

        Helper function!

        @param object symbol: the symbol
        @param int number: the frequency number
        @rtype: HuffmanNode
        """
        tree = HuffmanNode(symbol)
        tree.number = number
        return tree

    return_tree = HuffmanNode(None)  # Default tree is None
    _ordered_list = sort_freq_dict(freq_dict)
    if len(_ordered_list) == 0:  # If the input is empty
        return return_tree
    elif len(_ordered_list) == 1:  # If there is only one input freq
        return build_tree(_ordered_list[0][0], _ordered_list[0][1])
    elif len(_ordered_list) >= 2:  # If there is >= 2 freq dict:
        if len(_ordered_list) == 2:  # If there is just two of them:
            node1 = build_tree(_ordered_list[0][0], _ordered_list[0][1])
            node2 = build_tree(_ordered_list[1][0], _ordered_list[1][1])
            return create_tree(node1, node2)  # Create a tree with just 2 freq.
        while len(_ordered_list) >= 2:  # Loop though elements in the list
            # Until there is less than two element.
            first_stored_tree = _ordered_list[0][2]  # If there is a tree in the
            second_stored_tree = _ordered_list[1][2]  # list, make them temp
            if first_stored_tree and second_stored_tree:
                node2 = build_tree(_ordered_list[1][0], _ordered_list[1][1])
                return_tree = create_tree(first_stored_tree, node2)
                del _ordered_list[1], _ordered_list[0]  # Remove two records
                _ordered_list.insert(0, (None, return_tree.number, return_tree))
                # Add the new combined record and tree into the sorted list.
            elif first_stored_tree and second_stored_tree:
                node1 = build_tree(_ordered_list[0][0], _ordered_list[0][1])
                return_tree = create_tree(node1, second_stored_tree)
                del _ordered_list[1], _ordered_list[0]  # Remove two records
                _ordered_list.insert(0, (None, return_tree.number, return_tree))
                # Add the new combined record and tree into the sorted list.
            elif first_stored_tree and second_stored_tree:
                return_tree = create_tree(first_stored_tree, second_stored_tree)
                del _ordered_list[1], _ordered_list[0]  # Remove two records
                _ordered_list.insert(0, (None, return_tree.number, return_tree))
                # Add the new combined record and tree into the sorted list.
            else:  # Then both element in the list does not have a tree
                node1 = build_tree(_ordered_list[0][0], _ordered_list[0][1])
                node2 = build_tree(_ordered_list[1][0], _ordered_list[1][1])
                return_tree = create_tree(node1, node2)
                del _ordered_list[1], _ordered_list[0]
                _ordered_list.insert(0, (None, return_tree.number, return_tree))
            _ordered_list = sorted(_ordered_list, key=lambda tup: tup[1])
            # Sort the list after the insertion in the front
        if len(_ordered_list) == 1:  # If there is only one object left in list
                # It has to be the last root node, return it.
                return _ordered_list[0][2]


def sort_freq_dict(freq_dict):
    """Return the sorted version of freq_dict, with increasing order of
    frequency.

    It's a helper function to huffman_tree!

    @param dict(int,int) freq_dict: a frequency dictionary
    @rtype: list

    >>> freq = {2: 6, 3: 4}
    >>> t = sort_freq_dict(freq)
    >>> t == [(3,4,None),(2,6,None)]
    True
    """
    _intermediate = []
    for i,j in freq_dict.items():
        _intermediate.append((i,j,None))
    _output = sorted(_intermediate, key=lambda tup: tup[1])
    return _output


def merge_dict(dict1, dict2):
    """Merges the dict1 and dict2 together.
    @param dict(int,int) dict1: a frequency dictionary
    @param dict(int,int) dict2: a frequency dictionary
    @rtype: dict(int, int)
    """
    _temp = dict1.copy()
    _temp.update(dict2)
    return _temp

def get_codes(tree):
    """ Return a dict mapping symbols from tree rooted at HuffmanNode to codes.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: dict(int,str)

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> d = get_codes(tree)
    >>> d == {3: "0", 2: "1"}
    True
    """

    if tree.left is None and tree.right is None:
        return {tree.symbol: '"'+str() + '"'}
    elif tree is None:
        pass
    else:
        return tree.left



def number_nodes(tree):
    """ Number internal nodes in tree according to postorder traversal;
    start numbering at 0.

    @param HuffmanNode tree:  a Huffman tree rooted at node 'tree'
    @rtype: NoneType

    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(None, HuffmanNode(9), HuffmanNode(10))
    >>> tree = HuffmanNode(None, left, right)
    >>> number_nodes(tree)
    >>> tree.left.number
    0
    >>> tree.right.number
    1
    >>> tree.number
    2
    """

    def recursive_move(tree, count=0):
        if tree is None:
            return 0
        elif tree.left is None and tree.right is None:
            return 0
        else:
            if tree.left:
                count += recursive_move(tree.left, count)
            if tree.right:
                count += recursive_move(tree.right, count)
            tree.number = count
            count += 1
            return count

    recursive_move(tree, 0)


def avg_length(tree, freq_dict):
    """ Return the number of bits per symbol required to compress text
    made of the symbols and frequencies in freq_dict, using the Huffman tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: float

    >>> freq = {3: 2, 2: 7, 9: 1}
    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(9)
    >>> tree = HuffmanNode(None, left, right)
    >>> avg_length(tree, freq)
    1.9
    """
    # todo


def generate_compressed(text, codes):
    """ Return compressed form of text, using mapping in codes for each symbol.

    @param bytes text: a bytes object
    @param dict(int,str) codes: mappings from symbols to codes
    @rtype: bytes

    >>> d = {0: "0", 1: "10", 2: "11"}
    >>> text = bytes([1, 2, 1, 0])
    >>> result = generate_compressed(text, d)
    >>> [byte_to_bits(byte) for byte in result]
    ['10111000']
    >>> text = bytes([1, 2, 1, 0, 2])
    >>> result = generate_compressed(text, d)
    >>> [byte_to_bits(byte) for byte in result]
    ['10111001', '10000000']
    """
    # todo


def tree_to_bytes(tree):
    """ Return a bytes representation of the tree rooted at tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes

    The representation should be based on the postorder traversal of tree
    internal nodes, starting from 0.
    Precondition: tree has its nodes numbered.

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> number_nodes(tree)
    >>> list(tree_to_bytes(tree))
    [0, 3, 0, 2]
    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(5)
    >>> tree = HuffmanNode(None, left, right)
    >>> number_nodes(tree)
    >>> list(tree_to_bytes(tree))
    [0, 3, 0, 2, 1, 0, 0, 5]
    """
    # todo


def num_nodes_to_bytes(tree):
    """ Return number of nodes required to represent tree (the root of a
    numbered Huffman tree).

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes
    """
    return bytes([tree.number + 1])


def size_to_bytes(size):
    """ Return the size as a bytes object.

    @param int size: a 32-bit integer that we want to convert to bytes
    @rtype: bytes

    >>> list(size_to_bytes(300))
    [44, 1, 0, 0]
    """
    # little-endian representation of 32-bit (4-byte)
    # int size
    return size.to_bytes(4, "little")


def compress(in_file, out_file):
    """ Compress contents of in_file and store results in out_file.

    @param str in_file: input file whose contents we want to compress
    @param str out_file: output file, where we store our compressed result
    @rtype: NoneType
    """
    with open(in_file, "rb") as f1:
        text = f1.read()
    freq = make_freq_dict(text)
    tree = huffman_tree(freq)
    codes = get_codes(tree)
    number_nodes(tree)
    print("Bits per symbol:", avg_length(tree, freq))
    result = (num_nodes_to_bytes(tree) + tree_to_bytes(tree) +
              size_to_bytes(len(text)))
    result += generate_compressed(text, codes)
    with open(out_file, "wb") as f2:
        f2.write(result)


# ====================
# Functions for decompression


def generate_tree_general(node_lst, root_index):
    """ Return the root of the Huffman tree corresponding
    to node_lst[root_index].

    The function assumes nothing about the order of the nodes in the list.

    @param list[ReadNode] node_lst: a list of ReadNode objects
    @param int root_index: index in the node list
    @rtype: HuffmanNode

    >>> lst = [ReadNode(0, 5, 0, 7), ReadNode(0, 10, 0, 12), \
    ReadNode(1, 1, 1, 0)]
    >>> generate_tree_general(lst, 2)
    HuffmanNode(None, HuffmanNode(None, HuffmanNode(10, None, None), \
HuffmanNode(12, None, None)), \
HuffmanNode(None, HuffmanNode(5, None, None), HuffmanNode(7, None, None)))
    """
    # todo


def generate_tree_postorder(node_lst, root_index):
    """ Return the root of the Huffman tree corresponding
    to node_lst[root_index].

    The function assumes that the list represents a tree in postorder.

    @param list[ReadNode] node_lst: a list of ReadNode objects
    @param int root_index: index in the node list
    @rtype: HuffmanNode

    >>> lst = [ReadNode(0, 5, 0, 7), ReadNode(0, 10, 0, 12), \
    ReadNode(1, 0, 1, 0)]
    >>> generate_tree_postorder(lst, 2)
    HuffmanNode(None, HuffmanNode(None, HuffmanNode(5, None, None), \
HuffmanNode(7, None, None)), \
HuffmanNode(None, HuffmanNode(10, None, None), HuffmanNode(12, None, None)))
    """
    # todo


def generate_uncompressed(tree, text, size):
    """ Use Huffman tree to decompress size bytes from text.

    @param HuffmanNode tree: a HuffmanNode tree rooted at 'tree'
    @param bytes text: text to decompress
    @param int size: how many bytes to decompress from text.
    @rtype: bytes
    """
    # todo


def bytes_to_nodes(buf):
    """ Return a list of ReadNodes corresponding to the bytes in buf.

    @param bytes buf: a bytes object
    @rtype: list[ReadNode]

    >>> bytes_to_nodes(bytes([0, 1, 0, 2]))
    [ReadNode(0, 1, 0, 2)]
    """
    lst = []
    for i in range(0, len(buf), 4):
        l_type = buf[i]
        l_data = buf[i+1]
        r_type = buf[i+2]
        r_data = buf[i+3]
        lst.append(ReadNode(l_type, l_data, r_type, r_data))
    return lst


def bytes_to_size(buf):
    """ Return the size corresponding to the
    given 4-byte little-endian representation.

    @param bytes buf: a bytes object
    @rtype: int

    >>> bytes_to_size(bytes([44, 1, 0, 0]))
    300
    """
    return int.from_bytes(buf, "little")


def uncompress(in_file, out_file):
    """ Uncompress contents of in_file and store results in out_file.

    @param str in_file: input file to uncompress
    @param str out_file: output file that will hold the uncompressed results
    @rtype: NoneType
    """
    with open(in_file, "rb") as f:
        num_nodes = f.read(1)[0]
        buf = f.read(num_nodes * 4)
        node_lst = bytes_to_nodes(buf)
        # use generate_tree_general or generate_tree_postorder here
        tree = generate_tree_general(node_lst, num_nodes - 1)
        size = bytes_to_size(f.read(4))
        with open(out_file, "wb") as g:
            text = f.read()
            g.write(generate_uncompressed(tree, text, size))


# ====================
# Other functions

def improve_tree(tree, freq_dict):
    """ Improve the tree as much as possible, without changing its shape,
    by swapping nodes. The improvements are with respect to freq_dict.

    @param HuffmanNode tree: Huffman tree rooted at 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: NoneType

    >>> left = HuffmanNode(None, HuffmanNode(99), HuffmanNode(100))
    >>> right = HuffmanNode(None, HuffmanNode(101), \
    HuffmanNode(None, HuffmanNode(97), HuffmanNode(98)))
    >>> tree = HuffmanNode(None, left, right)
    >>> freq = {97: 26, 98: 23, 99: 20, 100: 16, 101: 15}
    >>> improve_tree(tree, freq)
    >>> avg_length(tree, freq)
    2.31
    """
    # todo

if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="huffman_pyta.txt")
    # TODO: Uncomment these when you have implemented all the functions
    # import doctest
    # doctest.testmod()

    import time

    mode = input("Press c to compress or u to uncompress: ")
    if mode == "c":
        fname = input("File to compress: ")
        start = time.time()
        compress(fname, fname + ".huf")
        print("compressed {} in {} seconds."
              .format(fname, time.time() - start))
    elif mode == "u":
        fname = input("File to uncompress: ")
        start = time.time()
        uncompress(fname, fname + ".orig")
        print("uncompressed {} in {} seconds."
              .format(fname, time.time() - start))

import cv2
import numpy as np
import heapq
from collections import defaultdict, Counter

# Huffman Tree Node
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freqs):
    priority_queue = [Node(char, freq) for char, freq in freqs.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    return priority_queue[0]

def build_codes(node, prefix='', codebook=defaultdict()):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encoding(image):
    # Flatten the image and count frequencies
    flat_image = image.flatten()
    freqs = Counter(flat_image)
    tree = build_huffman_tree(freqs)
    codes = build_codes(tree)

    # Encode the image
    encoded_image = ''.join(codes[pixel] for pixel in flat_image)
    return codes, encoded_image

def huffman_decoding(encoded_image, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ''
    decoded_image = []
    for bit in encoded_image:
        current_code += bit
        if current_code in reverse_codes:
            decoded_image.append(reverse_codes[current_code])
            current_code = ''
    return np.array(decoded_image).reshape(original_shape)

def main():
    # Load and prepare the image
    image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
    original_shape = image.shape

    # Perform Huffman encoding and decoding
    codes, encoded_image = huffman_encoding(image)
    decoded_image = huffman_decoding(encoded_image, codes)

    # Save or display the decoded image
    cv2.imwrite('decoded_image.png', decoded_image)

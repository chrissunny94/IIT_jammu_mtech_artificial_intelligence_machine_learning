import numpy as np
from collections import Counter
import heapq
import matplotlib.pyplot as plt

# Given 5x5 image
image = np.array([
    [0, 1, 1, 2, 2],
    [3, 3, 4, 4, 4],
    [5, 5, 5, 6, 6],
    [7, 7, 7, 7, 0],
    [1, 1, 2, 2, 3]
])

def compute_entropy(image):
    hist, _ = np.histogram(image, bins=np.arange(9), density=True)
    hist = hist[hist > 0]
    entropy = -np.sum(hist * np.log2(hist))
    return entropy

def huffman_tree(symbols_with_probs):
    heap = [[weight, [symbol, ""]] for symbol, weight in symbols_with_probs.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def histogram_equalization(image):
    flat = image.flatten()
    hist, bins = np.histogram(flat, bins=np.arange(9), density=False)
    cdf = hist.cumsum()
    cdf_normalized = cdf * 7 / cdf[-1]
    equalized_image = np.interp(flat, bins[:-1], cdf_normalized).reshape(image.shape)
    return equalized_image.astype(int)

# Step 1: Compute entropy of the original image
entropy = compute_entropy(image)
print(f"Entropy of the original image: {entropy:.4f}")

# Step 2: Feasibility of Huffman coding
symbol_counts = Counter(image.flatten())
total_pixels = image.size
symbol_probs = {k: v / total_pixels for k, v in symbol_counts.items()}
print("Symbol probabilities:", symbol_probs)

# Step 3: Huffman codes and tree
huffman_codes = huffman_tree(symbol_probs)
print("Huffman Codes:")
for p in huffman_codes:
    print(f"Symbol: {p[0]}, Code: {p[1]}")

# Step 4: Perform histogram equalization
equalized_image = histogram_equalization(image)
print("Equalized Image:\n", equalized_image)

# Recompute entropy and Huffman codes for the equalized image
equalized_entropy = compute_entropy(equalized_image)
print(f"Entropy of the equalized image: {equalized_entropy:.4f}")

equalized_symbol_counts = Counter(equalized_image.flatten())
equalized_symbol_probs = {k: v / total_pixels for k, v in equalized_symbol_counts.items()}

equalized_huffman_codes = huffman_tree(equalized_symbol_probs)
print("Huffman Codes after Histogram Equalization:")
for p in equalized_huffman_codes:
    print(f"Symbol: {p[0]}, Code: {p[1]}")

# Plot the original and equalized images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray', vmin=0, vmax=7)
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title("Equalized Image")
plt.imshow(equalized_image, cmap='gray', vmin=0, vmax=7)
plt.colorbar()

plt.show()

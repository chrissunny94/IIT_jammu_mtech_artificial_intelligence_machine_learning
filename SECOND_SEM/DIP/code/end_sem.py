import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import heapq

# Problem 1: Image Transformation (Hypothetical explanation, no specific implementation required)
def image_transformation_example():
    pass  # No code required for this problem

# Problem 2: Composite 3x3 Spatial Filter Mask
def composite_filter_example():
    # Composite filter mask
    composite_filter = np.array([
        [-1, -1, -1],
        [-1,  9, -1],
        [-1, -1, -1]
    ])
    return composite_filter

def apply_composite_filter(image):
    composite_filter = composite_filter_example()
    return cv2.filter2D(image, -1, composite_filter)

def fourier_transform_of_filter(filter_mask):
    dft = np.fft.fft2(filter_mask, s=(256, 256))
    dft_shifted = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(np.abs(dft_shifted))
    return magnitude_spectrum

# Problem 3: Unsharp Masking
def apply_box_filter(image):
    box_filter = np.ones((3, 3)) / 9.0
    return cv2.filter2D(image, -1, box_filter)

def unsharp_masking(image):
    smoothed_image = apply_box_filter(image)
    unsharp_mask = image - smoothed_image
    sharpened_image = image + unsharp_mask
    return sharpened_image

# Problem 4: Entropy and Huffman Coding
def calculate_entropy(image):
    unique, counts = np.unique(image, return_counts=True)
    probabilities = counts / np.sum(counts)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def build_huffman_tree(probabilities):
    heap = [[weight, [symbol, ""]] for symbol, weight in probabilities.items()]
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

def apply_histogram_equalization(image):
    return cv2.equalizeHist(image.astype(np.uint8))

def main():
    # Capture a frame from the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Problem 2: Composite 3x3 Spatial Filter Mask
    composite_filtered_image = apply_composite_filter(gray_frame)
    magnitude_spectrum = fourier_transform_of_filter(composite_filter_example())
    
    # Display the results for Problem 2
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(composite_filtered_image, cmap='gray')
    plt.title('Composite Filtered Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum of the Filter')
    plt.axis('off')
    plt.show()
    
    # Problem 3: Unsharp Masking
    unsharp_image = unsharp_masking(gray_frame)
    
    # Display the results for Problem 3
    plt.figure()
    plt.imshow(unsharp_image, cmap='gray')
    plt.title('Unsharp Masking Result')
    plt.axis('off')
    plt.show()
    
    # Problem 4: Entropy and Huffman Coding
    example_image = np.array([
        [0, 1, 2, 3, 4],
        [4, 5, 6, 7, 0],
        [1, 2, 3, 4, 5],
        [5, 6, 7, 0, 1],
        [2, 3, 4, 5, 6]
    ])
    
    entropy = calculate_entropy(example_image)
    print("Entropy of the example image:", entropy)
    
    probabilities = dict(Counter(example_image.flatten()))
    huffman_tree = build_huffman_tree(probabilities)
    print("Huffman Codes:", huffman_tree)
    
    equalized_image = apply_histogram_equalization(example_image)
    entropy_eq = calculate_entropy(equalized_image)
    print("Entropy after histogram equalization:", entropy_eq)
    
    probabilities_eq = dict(Counter(equalized_image.flatten()))
    huffman_tree_eq = build_huffman_tree(probabilities_eq)
    print("Huffman Codes after HE:", huffman_tree_eq)

if __name__ == "__main__":
    main()

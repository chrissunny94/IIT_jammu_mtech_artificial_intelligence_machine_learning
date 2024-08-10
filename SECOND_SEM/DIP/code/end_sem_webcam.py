import cv2
import numpy as np
import heapq
from collections import Counter
import matplotlib.pyplot as plt

# Composite Filter Construction
def composite_filter():
    gaussian_filter = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]) / 16

    laplacian_filter = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ])

    composite_filter = gaussian_filter + laplacian_filter
    return composite_filter

# Compute Fourier Transform
def compute_fourier_transform(filter):
    fourier_transform = np.fft.fft2(filter)
    fourier_transform_shifted = np.fft.fftshift(fourier_transform)
    return fourier_transform_shifted

# Plot 1D Profiles
def plot_profiles(fourier_transform):
    center = np.array(fourier_transform.shape) // 2

    H_w1_0 = np.abs(fourier_transform[center[0], :])
    H_w1_pi = np.abs(fourier_transform[:, center[1]])
    H_0_w2 = np.abs(fourier_transform[:, center[0]])
    H_pi_w2 = np.abs(fourier_transform[center[1], :])

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 2, 1)
    plt.plot(H_w1_0)
    plt.title("H(ω1, 0)")

    plt.subplot(2, 2, 2)
    plt.plot(H_w1_pi)
    plt.title("H(ω1, π)")

    plt.subplot(2, 2, 3)
    plt.plot(H_0_w2)
    plt.title("H(0, ω2)")

    plt.subplot(2, 2, 4)
    plt.plot(H_pi_w2)
    plt.title("H(π, ω2)")

    plt.tight_layout()
    plt.show()

# Unsharp Masking
def unsharp_masking(image):
    box_filter = np.ones((3, 3)) / 9.0
    smoothed_image = cv2.filter2D(image, -1, box_filter)
    unsharp_mask = image - smoothed_image
    sharpened_image = image + unsharp_mask
    return sharpened_image

# Compute Entropy
def compute_entropy(image):
    hist, _ = np.histogram(image, bins=np.arange(9), density=True)
    hist = hist[hist > 0]
    entropy = -np.sum(hist * np.log2(hist))
    return entropy

# Huffman Tree and Coding
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

# Histogram Equalization
def histogram_equalization(image):
    flat = image.flatten()
    hist, bins = np.histogram(flat, bins=np.arange(9), density=False)
    cdf = hist.cumsum()
    cdf_normalized = cdf * 7 / cdf[-1]
    equalized_image = np.interp(flat, bins[:-1], cdf_normalized).reshape(image.shape)
    return equalized_image.astype(np.uint8)  # Ensure the result is in uint8

# Main function to capture and process webcam image
def main():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Composite Filter
        composite_filter_matrix = composite_filter()
        filtered_image = cv2.filter2D(gray_frame, -1, composite_filter_matrix)
        
        # Compute Fourier Transform
        fourier_transform = compute_fourier_transform(composite_filter_matrix)
        plot_profiles(fourier_transform)
        
        # Apply Unsharp Masking
        sharpened_image = unsharp_masking(gray_frame)
        
        # Compute Entropy
        entropy = compute_entropy(gray_frame)
        
        # Huffman Coding
        flat = gray_frame.flatten()
        symbol_counts = Counter(flat)
        total_pixels = flat.size
        symbol_probs = {k: v / total_pixels for k, v in symbol_counts.items()}
        huffman_codes = huffman_tree(symbol_probs)
        
        print("Entropy of the image:", entropy)
        print("Huffman Codes:")
        for p in huffman_codes:
            print(f"Symbol: {p[0]}, Code: {p[1]}")
        
        # Histogram Equalization
        equalized_image = histogram_equalization(gray_frame)
        entropy_equalized = compute_entropy(equalized_image)
        
        # Huffman Coding after Histogram Equalization
        flat_equalized = equalized_image.flatten()
        symbol_counts_equalized = Counter(flat_equalized)
        total_pixels_equalized = flat_equalized.size
        symbol_probs_equalized = {k: v / total_pixels_equalized for k, v in symbol_counts_equalized.items()}
        huffman_codes_equalized = huffman_tree(symbol_probs_equalized)
        
        print("Entropy after Histogram Equalization:", entropy_equalized)
        print("Huffman Codes after Histogram Equalization:")
        for p in huffman_codes_equalized:
            print(f"Symbol: {p[0]}, Code: {p[1]}")
        
        # Display Images
        cv2.imshow('Original Image', gray_frame)
        cv2.imshow('Filtered Image', filtered_image)
        cv2.imshow('Sharpened Image', sharpened_image)
        cv2.imshow('Equalized Image', equalized_image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

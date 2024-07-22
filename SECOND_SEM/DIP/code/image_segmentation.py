import cv2
import numpy as np
import matplotlib.pyplot as plt

def capture_webcam_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Error: Could not read frame.")
        return None

    return frame

def apply_thresholding(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, global_thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return global_thresh, adaptive_thresh

def apply_region_growing(image, seed_point):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask = np.zeros((gray.shape[0] + 2, gray.shape[1] + 2), np.uint8)
    connectivity = 8  # Connectivity parameter for region growing
    flags = connectivity | cv2.FLOODFILL_FIXED_RANGE
    cv2.floodFill(gray, mask, seed_point, 255, (10,), (10,), flags)
    return mask[1:-1, 1:-1]  # Removing the added border

def apply_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def display_images(images, titles):
    plt.figure(figsize=(15, 5))

    for i in range(len(images)):
        plt.subplot(1, len(images), i + 1)
        if len(images[i].shape) == 2:
            plt.imshow(images[i], cmap='gray')
        else:
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')

    plt.show()

def main():
    frame = capture_webcam_image()
    if frame is not None:
        global_thresh, adaptive_thresh = apply_thresholding(frame)
        seed_point = (int(frame.shape[1] / 2), int(frame.shape[0] / 2))
        region_grown = apply_region_growing(frame, seed_point)
        edges = apply_edge_detection(frame)
        
        images = [frame, global_thresh, adaptive_thresh, region_grown, edges]
        titles = ['Original Image', 'Global Thresholding', 'Adaptive Thresholding', 'Region Growing', 'Edge Detection']
        display_images(images, titles)

if __name__ == "__main__":
    main()

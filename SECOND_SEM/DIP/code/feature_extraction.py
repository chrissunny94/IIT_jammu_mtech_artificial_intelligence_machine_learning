import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops, local_binary_pattern

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

def sobel_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(sobel_x, sobel_y)
    return magnitude

def canny_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def texture_analysis(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcm = greycomatrix(gray, [1], [0], symmetric=True, normed=True)
    contrast = greycoprops(glcm, 'contrast')[0, 0]
    correlation = greycoprops(glcm, 'correlation')[0, 0]
    return contrast, correlation

def local_binary_patterns(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp = local_binary_pattern(gray, P=8, R=1, method='uniform')
    return lbp

def find_contours(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def hough_transform(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)
    return lines

def display_images(images, titles):
    plt.figure(figsize=(15, 10))

    for i in range(len(images)):
        plt.subplot(2, 3, i + 1)
        if images[i] is None:
            continue
        plt.imshow(images[i], cmap='gray' if len(images[i].shape) == 2 else None)
        plt.title(titles[i])
        plt.axis('off')

    plt.show()

def main():
    frame = capture_webcam_image()
    if frame is not None:
        sobel_edges = sobel_edge_detection(frame)
        canny_edges = canny_edge_detection(frame)
        contrast, correlation = texture_analysis(frame)
        lbp = local_binary_patterns(frame)
        contours = find_contours(frame)
        lines = hough_transform(frame)

        titles = [
            'Original Image',
            'Sobel Edges',
            'Canny Edges',
            'Local Binary Patterns',
            f'Texture - Contrast: {contrast:.2f}, Correlation: {correlation:.2f}'
        ]

        images = [frame, sobel_edges, canny_edges, lbp, contours]
        display_images(images, titles)

if __name__ == "__main__":
    main()

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

def enhance_image(image):
    # Convert to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Color space transformation: RGB to HSV
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Histogram equalization on the HSV value channel
    h, s, v = cv2.split(image_hsv)
    v_eq = cv2.equalizeHist(v)
    image_hsv_eq = cv2.merge([h, s, v_eq])
    image_rgb_eq = cv2.cvtColor(image_hsv_eq, cv2.COLOR_HSV2RGB)

    # Color filtering: Enhance red color in the image (example)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(image_hsv, lower_red, upper_red)
    result = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)

    return image_rgb, image_hsv, image_rgb_eq, result

def display_images(images):
    titles = ['Original Image', 'HSV Image', 'Histogram Equalized', 'Red Color Enhanced']

    plt.figure(figsize=(15, 5))

    for i in range(len(images)):
        plt.subplot(1, 4, i + 1)
        if i == 1:  # HSV Image
            plt.imshow(images[i], cmap='hsv')
        else:
            plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')

    plt.show()

def main():
    frame = capture_webcam_image()
    if frame is not None:
        images = enhance_image(frame)
        display_images(images)

if __name__ == "__main__":
    main()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to perform histogram equalization
def histogram_equalization(image):
    return cv2.equalizeHist(image)

# Function to perform histogram stretching
def histogram_stretching(image):
    min_val, max_val = np.percentile(image, (2, 98))
    stretched = cv2.normalize(image, None, min_val, max_val, cv2.NORM_MINMAX)
    return stretched

# Function to apply an averaging filter
def averaging_filter(image):
    return cv2.blur(image, (5, 5))

# Function to apply a median filter
def median_filter(image):
    return cv2.medianBlur(image, 5)

# Function to apply Ideal Low-Pass Filter in Frequency Domain
def ideal_low_pass_filter(image, radius=30):
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow-radius:crow+radius, ccol-radius:ccol+radius] = 1
    
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    
    cv2.normalize(img_back, img_back, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(img_back)

# Function to apply Butterworth Low-Pass Filter in Frequency Domain
def butterworth_low_pass_filter(image, radius=30, n=2):
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols, 2), np.float32)
    
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow)**2 + (j - ccol)**2)
            mask[i, j] = 1 / (1 + (distance / radius)**(2 * n))
    
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    
    cv2.normalize(img_back, img_back, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(img_back)

# Capture a frame from the webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

# Convert frame to grayscale
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply image enhancement techniques
hist_eq_image = histogram_equalization(gray_frame)
hist_stretch_image = histogram_stretching(gray_frame)
avg_filtered_image = averaging_filter(gray_frame)
median_filtered_image = median_filter(gray_frame)
ideal_low_pass_image = ideal_low_pass_filter(gray_frame)
butterworth_low_pass_image = butterworth_low_pass_filter(gray_frame)

# Display the results in a Matplotlib multi-image canvas
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].imshow(gray_frame, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(hist_eq_image, cmap='gray')
axes[0, 1].set_title('Histogram Equalization')
axes[0, 1].axis('off')

axes[1, 0].imshow(ideal_low_pass_image, cmap='gray')
axes[1, 0].set_title('Ideal Low-Pass Filter')
axes[1, 0].axis('off')

axes[1, 1].imshow(butterworth_low_pass_image, cmap='gray')
axes[1, 1].set_title('Butterworth Low-Pass Filter')
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()

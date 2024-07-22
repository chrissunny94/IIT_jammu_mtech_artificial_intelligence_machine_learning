import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import feature

def plot_image(img, title="Image", cmap='gray'):
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.axis('off')
    plt.show()

def image_sampling_quantization(img, scale_factor=0.5, num_levels=256):
    img_resized = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    img_quantized = (img_resized // (256 // num_levels)) * (256 // num_levels)
    return img_resized, img_quantized

def histogram_equalization(img):
    return cv2.equalizeHist(img)

def spatial_filtering(img, kernel):
    return cv2.filter2D(img, -1, kernel)

def frequency_domain_filtering(img, filter_type='ideal', cutoff=30):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    
    rows, cols = img.shape
    crow, ccol = rows // 2 , cols // 2

    if filter_type == 'ideal':
        mask = np.zeros((rows, cols), np.uint8)
        mask[crow - cutoff:crow + cutoff, ccol - cutoff:ccol + cutoff] = 1
    elif filter_type == 'butterworth':
        d0 = cutoff
        n = 2
        u, v = np.ogrid[:rows, :cols]
        distance = np.sqrt((u - crow)**2 + (v - ccol)**2)
        mask = 1 / (1 + (distance / d0)**(2 * n))
    
    fshift *= mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    return img_back

def color_processing(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return hsv_img, rgb_img

def morphological_processing(img):
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
    dilation = cv2.dilate(img, kernel, iterations=1)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return erosion, dilation, opening, closing

def edge_detection(img):
    edges = cv2.Canny(img, 100, 200)
    return edges

def feature_extraction(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = feature.canny(gray_img)
    return edges

def image_compression(img, quality=90):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    result, encimg = cv2.imencode('.jpg', img, encode_param)
    decimg = cv2.imdecode(encimg, 1)
    return decimg

def image_segmentation(img, threshold=127):
    _, segmented_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return segmented_img

def plot_fourier_transform(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    plt.figure(figsize=(6, 6))
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Fourier Transform')
    plt.axis('off')
    plt.show()

def main():
    # Start video capture
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Display the original frame
        cv2.imshow('Original Frame', frame)
        
        # Image Sampling and Quantization
        resized_img, quantized_img = image_sampling_quantization(gray_frame)
        plot_image(resized_img, title="Resized Image")
        plot_image(quantized_img, title="Quantized Image")
        
        # Histogram Equalization
        equalized_img = histogram_equalization(gray_frame)
        plot_image(equalized_img, title="Equalized Image")
        
        # Spatial Filtering
        kernel = np.ones((3, 3), np.float32) / 9
        filtered_img = spatial_filtering(gray_frame, kernel)
        plot_image(filtered_img, title="Spatial Filtered Image")
        
        # Frequency Domain Filtering
        filtered_freq_img = frequency_domain_filtering(gray_frame, filter_type='butterworth', cutoff=30)
        plot_image(filtered_freq_img, title="Frequency Domain Filtered Image")
        
        # Color Processing
        hsv_img, rgb_img = color_processing(frame)
        plot_image(hsv_img, title="HSV Image")
        plot_image(rgb_img, title="RGB Image")
        
        # Morphological Processing
        binary_img = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)[1]
        erosion, dilation, opening, closing = morphological_processing(binary_img)
        plot_image(erosion, title="Erosion")
        plot_image(dilation, title="Dilation")
        plot_image(opening, title="Opening")
        plot_image(closing, title="Closing")
        
        # Edge Detection
        edges = edge_detection(gray_frame)
        plot_image(edges, title="Edges Detected")
        
        # Feature Extraction
        features = feature_extraction(frame)
        plot_image(features, title="Features Extracted")
        
        # Image Compression
        compressed_img = image_compression(frame)
        plot_image(compressed_img, title="Compressed Image")
        
        # Image Segmentation
        segmented_img = image_segmentation(gray_frame)
        plot_image(segmented_img, title="Segmented Image")
        
        # Fourier Transform Plot
        plot_fourier_transform(gray_frame)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

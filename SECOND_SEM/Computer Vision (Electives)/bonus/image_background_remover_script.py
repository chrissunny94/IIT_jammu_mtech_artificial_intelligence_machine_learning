import cv2
import numpy as np
import os

def remove_background(image_path, output_dir):
    """Removes the background from an image using a simple contour-based approach.

    Args:
        image_path: Path to the input image.
        output_dir: Directory to save the output image.
    """

    try:
        # Read the image
        original_image = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Thresholding
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)

        # Create a mask
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [largest_contour], -1, 255, -1)

        # Apply the mask to the original image
        result = cv2.bitwise_and(original_image, original_image, mask=mask)

        # Create a white background
        background = np.full_like(original_image, 255)

        # Combine the result with the white background
        final_image = cv2.bitwise_or(result, background)

        # Get the output file path
        output_path = os.path.join(output_dir, os.path.basename(image_path))

        # Save the image
        cv2.imwrite(output_path, final_image)

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

def process_folder(input_dir, output_dir):
    """Processes images in a folder and saves the results in a new folder.

    Args:
        input_dir: Path to the input folder.
        output_dir: Path to the output folder.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.jpg', '.JPG', '.png')):
                image_path = os.path.join(root, file)
                relative_path = os.path.relpath(image_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                print(image_path)
                remove_background(image_path, output_dir)

# Example usage
input_folder = "/Users/christhaliyath/Google Drive/My Drive/ONGOING_PROJECTS/WOODTECH/JAISON/Original_images/"
output_folder = "/Users/christhaliyath/Google Drive/My Drive/ONGOING_PROJECTS/WOODTECH/Background_removed"
process_folder(input_folder, output_folder)
import cv2
import numpy as np

def stereo_rectify_and_estimate_depth(img1_path, img2_path):
    """
    Rectifies a stereo image pair and estimates depth maps (single image,
    potentially noisy due to uncalibrated setup).

    Args:
        img1_path (str): Path to the first stereo image.
        img2_path (str): Path to the second stereo image.

    Returns:
        tuple: A tuple containing the rectified left and right images (img1_rect, img2_rect).
    """

    # Load images
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # Feature detection and matching (SIFT or ORB for robustness)
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # Match features using FLANN matcher (consider Brute-Force for simplicity)
    flann = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))
    matches = flann.knnMatch(des1, des2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7*n.distance:
            good_matches.append(m)

    # Draw matches for visualization (optional)
    img_matches = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_matches, None, flags=2)
    cv2.imshow('Matches', img_matches)
    cv2.waitKey(0)

    # Fundamental matrix estimation
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    F, mask = cv2.findFundamentalMat(src_pts, dst_pts, cv2.FM_RANSAC)

    # Rectification (assuming uncalibrated cameras)
    img_size = img1.shape[::-1]  # Get image size (width, height)
    H1, H2, d = cv2.stereoRectifyUncalibrated(src_pts, dst_pts, F, img_size, None, None, 5.0)

    # Rectify images
    img1_rect = cv2.warpPerspective(img1, H1, img_size)
    img2_rect = cv2.warpPerspective(img2, H2, img_size)

    # Depth map estimation (single image, potentially noisy)
    # Consider Semi-Global Matching (SGM) or PatchMatch Stereo,
    # but be aware of limitations due to uncalibrated setup.

    # Display rectified images and potentially estimated depth maps here

    return img1_rect, img2_rect

# Example usage
img1_rect, img2_rect = stereo_rectify_and_estimate_depth('image1.jpg', 'image2.jpg')
cv2.imshow('Rectified Image 1', img1_rect)
cv2.imshow('Rectified Image 2', img2_rect)
cv2.waitKey(0)
cv2.destroyAllWindows()

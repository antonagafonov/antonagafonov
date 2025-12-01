import cv2
import numpy as np

def crop_top_opencv(input_path, output_path, crop_ratio=0.2):
    """
    Crop the top portion of an image using OpenCV
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the cropped image
        crop_ratio (float): Ratio of the image height to keep from top (0.4 = top 40%)
    """
    # Read the image
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not load image from {input_path}")
        return None
    
    # Get image dimensions
    height, width = img.shape[:2]
    print(f"Original image shape: {img.shape}")
    
    crop_height = int(height*0.8)
    # Crop the top portion of the image
    cropped_img = img[:crop_height, :]  # Keep top crop_height rows, all columns
    print(f"After cropping top {crop_ratio*100}%: {cropped_img.shape}")
    
    # Save the cropped image
    cv2.imwrite(output_path, cropped_img)
    
    print(f"Original size: {width}x{height}")
    print(f"Cropped size: {width}x{crop_height}")
    print(f"Image saved to: {output_path}")
    
    return cropped_img

# Usage example
if __name__ == "__main__":
    input_image = "/home/ai4ia/antonagafonov/images/profile_photo2.png"  # Update with your new image path
    output_image = "/home/ai4ia/antonagafonov/images/cropped_profile_photo2.png"  # Update with your desired output path
    
    # Crop top 40%
    crop_top_opencv(input_image, output_image, crop_ratio=0.4)
    
    # Display the result (optional)
    result = cv2.imread(output_image)
    if result is not None:
        cv2.imshow('Top Cropped Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
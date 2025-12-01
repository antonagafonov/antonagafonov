import cv2
import numpy as np

def crop_left_opencv(input_path, output_path, crop_ratio=0.5):
    """
    Crop the left side of an image using OpenCV and rescale by dividing by 7
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the cropped image
        crop_ratio (float): Ratio of the image to keep (0.5 = left half)
    """
    # Read the image
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not load image from {input_path}")
        return None
    
    # Get image dimensions
    height, width = img.shape[:2]
    print(f"Original image shape: {img.shape}")
    
    # Rescale the image by dividing by 7
    new_height = height // 7
    new_width = width // 7
    resized_img = cv2.resize(img, (new_width, new_height))
    print(f"After rescaling by 7: {resized_img.shape}")
    
    # Save the rescaled image
    cv2.imwrite(output_path, resized_img)
    
    print(f"Original size: {width}x{height}")
    print(f"Final size: {new_width}x{new_height}")
    print(f"Image saved to: {output_path}")
    
    return resized_img

# Usage example
if __name__ == "__main__":
    input_image = "/home/ai4ia/antonagafonov/images/car_banner.jpg"
    output_image = "/home/ai4ia/antonagafonov/images/car_banner_cropped.jpg"
    
    # Rescale by dividing by 7
    crop_left_opencv(input_image, output_image)
    
    # Display the result (optional)
    result = cv2.imread(output_image)
    if result is not None:
        cv2.imshow('Rescaled Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
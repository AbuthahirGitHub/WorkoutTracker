import cv2

def preprocess_frame(frame):
    """
    Handles frame preprocessing tasks such as resizing and color conversion.

    Args:
        frame: The input frame to be preprocessed.

    Returns:
        The preprocessed frame.
    """
    # Check if the frame is a color image (3 channels)
    if len(frame.shape) == 3 and frame.shape[2] == 3:
        # Convert BGR color space to RGB color space
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Check if the frame is a grayscale image (1 channel)
    elif len(frame.shape) == 2:
        # Convert grayscale image to RGB color space
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
    else:
        # Raise an error for unsupported frame format
        raise ValueError("Unsupported frame format")

    # Define the desired width and height
    new_width = 640
    new_height = 480
    
    # Perform additional preprocessing tasks here (e.g., resizing)
    # Resize the frame to a specific width and height
    frame = cv2.resize(frame, (new_width, new_height))

    return frame

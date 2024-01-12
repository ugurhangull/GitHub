import cv2
import numpy as np

img = cv2.imread("/Users/ugurhangul/Desktop/untitled folder/ex1.png")

if img is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize the image
    resized_img = cv2.resize(gray_img, (786, 423))

    # Apply binary thresholding to the image
    _, thresholded_img = cv2.threshold(resized_img, 150, 255, cv2.THRESH_BINARY)





 
    # Apply adaptive thresholding to the image
    adaptive_thresholded_img = cv2.adaptiveThreshold(resized_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 35)






    # Apply sharpining to the image

    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened_img = cv2.filter2D(adaptive_thresholded_img, -1, kernel_sharpening)






    





    # Fill in gaps using morphological operations (opening)
    kernel = np.ones((3,4), np.uint8)
    opened_img = cv2.morphologyEx(sharpened_img, cv2.MORPH_OPEN, kernel)






    # Display the original, processed, and filled images
    cv2.imshow("Original Image", img)
    cv2.imshow("Thresholded Image", thresholded_img)
    cv2.imshow("Sharpened Image", sharpened_img)
   
    cv2.imshow("Filled Image", opened_img)

    # Wait for a key press before closing the windows
    cv2.waitKey(0)

    # Close the windows
    cv2.destroyAllWindows()

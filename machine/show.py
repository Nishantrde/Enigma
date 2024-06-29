import cv2

# Load an image from file
image_path = 'C:/Users/pc/Downloads/qr_here.png'
image = cv2.imread(image_path)

# Resize the image
new_width = 300  # New width
new_height = 300  # New height
resized_image = cv2.resize(image, (new_width, new_height))

# Display the resized image
cv2.imshow('Enigma', resized_image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()

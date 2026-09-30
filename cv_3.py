import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("images (3).jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image. Check the filename/path.")
    exit()

# Convert BGR image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)         

# Apply binary threshold
T = 127
ret, result = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)

# Create figure
plt.figure(figsize=(15, 5))

# Step 1: Original Image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Step 1: Original Image")
plt.axis("off")

# Step 2: Grayscale Image
plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Step 2: Grayscale Image")
plt.axis("off")

# Step 3: Threshold Result
plt.subplot(1, 3, 3)
plt.imshow(result, cmap="gray")
plt.title(f"Step 3: Threshold Result (T={T})")
plt.axis("off")

# Display everything
plt.tight_layout()
plt.show()

# Print information
print(f"Threshold value used: {T}")
print("Pixels in result: only 0 and 255")
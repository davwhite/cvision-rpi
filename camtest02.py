import time
import picamera

# Create an instance of the PiCamera class
camera = picamera.PiCamera()

# Set camera resolution (optional)
camera.resolution = (640, 480)

# Allow the camera to warm up
time.sleep(2)

# Capture an image and save it to a file
image_file = 'image.jpg'
camera.capture(image_file)

# Print a message indicating the capture is complete
print(f"Image captured and saved to '{image_file}'")

# Release resources
camera.close()


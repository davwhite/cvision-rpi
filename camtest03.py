#!/usr/bin/python
import time
import picamera
import requests

# Create an instance of the PiCamera class
camera = picamera.PiCamera()

# Set camera resolution (optional)
camera.resolution = (640, 480)

# Allow the camera to warm up
time.sleep(2)

# Generate a unique filename using timestamp
timestamp = time.strftime('%Y%m%d-%H%M%S')
image_file = f'image_{timestamp}.jpg'

# Capture an image and save it to the unique filename
camera.capture(image_file)

# Define the RESTful endpoint URL
endpoint_url = 'http://coco-model-rt-flyingthings-standalone.apps.ocpbare.davenet.local/detect'

# Prepare the file data in the same format as 'curl'
files = {
    'file': (image_file, open(image_file, 'rb'), 'image/jpeg')
}

# Send the image file to the endpoint
response = requests.post(endpoint_url, files=files, headers={'accept': 'application/json'})

# Print the JSON response
print(response.json())

# Release resources
camera.close()


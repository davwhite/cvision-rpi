#!/usr/bin/python
import time
import picamera
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL/TLS certificate verification warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Create an instance of the PiCamera class
camera = picamera.PiCamera()

# Set camera resolution (optional)
camera.resolution = (640, 480)

# Allow the camera to warm up
# time.sleep(1)

# Capture an image and save it to a file
image_file = 'image.jpg'
camera.capture(image_file)

# Define the RESTful endpoint URL
endpoint_url = 'https://model-b-rt-flyingthings-standalone.apps.ocp4.davenet.local/detect'

# Prepare the file data in the same format as 'curl'
files = {
    'file': (image_file, open(image_file, 'rb'), 'image/jpeg')
}

# Send the image file to the endpoint
response = requests.post(endpoint_url, files=files, headers={'accept': 'application/json'}, verify=False)

# Print the JSON response
print(response.json())

# Release resources
camera.close()


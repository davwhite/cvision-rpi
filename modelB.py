#!/usr/bin/python
import os
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

# Define the RESTful endpoint URL
endpoint_url = 'https://model-b-rt-flyingthings-standalone.apps.ocp4.davenet.local'

# Allow the camera to warm up
# time.sleep(1)

def take_picture(image_file):
    print("taken")
    # Capture an image and save it to a file
    camera.capture(image_file)
    return image_file

def identify_picture(image_file):
    # Prepare the file data in the same format as 'curl'
    files = {
        'file': (image_file, open(image_file, 'rb'), 'image/jpeg')
    }
    # Send the image file to the endpoint
    response = requests.post(endpoint_url + "/detect", files=files, headers={'accept': 'application/json'}, verify=False)
    return response

def save_image_from_endpoint(url, save_path, image_name):
    try:
        # Send GET request to the endpoint
        response = requests.get(url + "/uploads/get/image/" + image_name, stream=True, verify=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Create the save directory if it doesn't exist
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # Save the image to disk as "detected.jpg"
            save_filename = os.path.join(save_path, "detected.jpg")
            with open(save_filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

            print("Image saved successfully as 'detected.jpg'.")
        else:
            print("Error: Could not retrieve the image.")

    except requests.exceptions.RequestException as e:
        print("Error: An exception occurred while retrieving the image.")
        print(e)

    except requests.exceptions.RequestException as e:
        print("Error: An exception occurred while retrieving the image.")
        print(e)

mypic_filename = "image.jpg"
mypic = take_picture(mypic_filename)
mycar = identify_picture(mypic)

# Print the JSON response
print(mycar.json())

# Save the inferred image
save_image_from_endpoint(endpoint_url, "/home/davwhite/workspace/picam", mypic_filename)

# Release resources
camera.close()


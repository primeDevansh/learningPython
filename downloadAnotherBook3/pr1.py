import requests

# Base URL with placeholder for numbers
base_url = "https://image.slidesharecdn.com/prmynotes-200706105258/75/BTech-Pattern-Recognition-Notes-{}-2048.jpg"

# Directory to save images
output_dir = "./images/"

# Create the output directory if it doesn't exist
import os
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop to download images
for i in range(1, 31):
    image_url = base_url.format(i)
    image_path = os.path.join(output_dir, f"image_{i}.jpg")

    try:
        print(f"Downloading image {i}...")
        response = requests.get(image_url, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the image
            with open(image_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image {i} saved as {image_path}")
        else:
            print(f"Failed to download image {i}. HTTP Status: {response.status_code}")

    except Exception as e:
        print(f"An error occurred while downloading image {i}: {e}")

print("Download process completed.")


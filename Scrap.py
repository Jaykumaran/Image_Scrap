from selenium import webdriver
import requests
import os

# Set up Selenium web driver
driver = webdriver.Chrome("./chromedriver.exe")

# Define the search query
search_query = "cats"  # Replace with your desired search query

# Navigate to the Google Images search results page
driver.get(f"https://www.google.com/search?q={search_query}&tbm=isch")

# Find all the image elements on the page
image_elements = driver.find_elements_by_css_selector("img.rg_i")

# Create a directory to store the downloaded images
os.makedirs("images", exist_ok=True)

# Iterate over the image elements and download the images
for index, image_element in enumerate(image_elements):
    # Get the source URL of the image
    image_url = image_element.get_attribute("src")

    # Download the image using requests library
    response = requests.get(image_url)

    # Save the image to the directory
    with open(f"images/image{index}.jpg", "wb") as file:
        file.write(response.content)
        print(f"Image {index} downloaded successfully.")

# Close the browser
driver.quit()

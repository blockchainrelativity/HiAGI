# Import necessary libraries
import io
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from PIL import Image

# Define the ID of the file you want to download
file_id = "YOUR_FILE_ID"

# Define the name of the file you want to save the image as
filename = "image.jpg"

# Define the directory where you want to save the image file
directory = "/path/to/your/directory/"

# Authenticate to Google Drive API
creds_path = '/path/to/your/credentials.json'

def import_image_from_drive(file_id, filename, directory, creds_path):
    """
    Imports an image file from Google Drive and saves it to a local directory.
    Returns the image file as a bytes object.
    """
    
    # Authenticate to Google Drive API
    creds = Credentials.from_authorized_user_file(creds_path)

    # Build the Drive API client
    service = build('drive', 'v3', credentials=creds)

    try:
        # Call the Drive API to get the file data
        file = service.files().get(fileId=file_id).execute()

        # Get the file data and download the file
        data = file.get('content')
        if data:
            image = Image.open(io.BytesIO(data))
            image.save(os.path.join(directory, filename))
            print(f"Image saved as {filename} in {directory}")
            return data

    except HttpError as error:
        print(f"An error occurred: {error}")

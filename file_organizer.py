import os
import shutil


def organize_files_by_type(directory):
    # List all files in the given directory
    for filename in os.listdir(directory):
        # Get the full file path
        file_path = os.path.join(directory, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = filename.split('.')[-1]

            # Create a folder name based on the file extension
            folder_name = file_extension + "_files"
            folder_path = os.path.join(directory, folder_name)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file into the corresponding folder
            shutil.move(file_path, os.path.join(folder_path, filename))


# Example usage:
organize_files_by_type("/Users/abdifatah/Desktop")

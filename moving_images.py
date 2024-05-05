import os
import shutil

def move_images(source_dir, destination_dir):
    # Make sure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # Get a list of files in the source directory
    files = os.listdir(source_dir)
    
    # Iterate through each file in the source directory
    for file in files:
        # Check if the file is an image (you can add more image extensions if needed)
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            # Build the full path of the source file
            source_file = os.path.join(source_dir, file)
            
            # Build the full path of the destination file
            destination_file = os.path.join(destination_dir, file)
            
            # Move the file to the destination directory
            shutil.move(source_file, destination_file)
            print(f"Moved {file} to {destination_dir}")

# Example usage
source_directory = r'C:\Users\amarn\Downloads\drones.v1i.voc\test'
destination_directory = r'D:\AMAR_Gitwork\jetson-train\data\toys\JPEGImages'

move_images(source_directory, destination_directory)

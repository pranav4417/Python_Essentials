"""
FileBatcher - A Python Program for Organizing Files in Batches
Developed by Pranav Kandakurthi

Copyright (c) 2025, Pranav Kandakurthi
All rights reserved.

This program is free to use for personal and educational purposes.

This program allows users to move or copy files into batches, simplifying file organization.

Time Complexity:
- Listing Files in Source Folder (`get_all_files`): O(n), where n is the number of files in the source folder.
- Creating Batches: O(b), where b is the number of batches (n / batch_size). Folder creation is relatively fast.
- Copying/Moving Files (`copy_or_move_file`): O(n), where n is the number of files being processed.
- Progress Bar and Spinner: O(n), since the spinner and progress bar update as each file is processed.

Overall Time Complexity: O(n), where n is the number of files being processed.

Space Complexity:
- O(n), where n is the number of files stored in memory (list of files) and the number of directories created for batches.
"""

import os
import shutil
import time
import sys
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm  # For progress bar
from concurrent.futures import ThreadPoolExecutor  # For parallel processing
import signal  # For handling interrupt (Ctrl + C)

# Clear screen function for better readability
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to open file explorer and get the directory path
def select_directory(title="Select a Folder"):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory(title=title)  # Open file explorer
    return folder_selected

# Function to get the action (copy or move) from the user
def get_action():
    while True:
        action = input("\nChoose the reqired operation \n1.Copy(Enter 'c') \n2.Move(Enter 'm')").strip().lower()
        if action in ['c', 'm']:
            return action
        else:
            print("Invalid input! Please enter 'c' to copy or 'm' to move.")

# Function to ask for batch size and ensure it's a valid integer
def get_batch_size():
    while True:
        try:
            batch_size = int(input("\nEnter the number of files to be grouped per batch: "))
            if batch_size > 0:
                return batch_size
            else:
                print("Please enter a positive integer for batch size.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Define source and destination folder paths using File Explorer
def select_folders():
    print("Please select the source folder (where your files are stored):")
    source_folder = select_directory(title="Select Source Folder")
    if not source_folder:
        print("No source folder selected. Exiting program.")
        sys.exit(1)

    print("Please select the destination folder (where the files will be grouped):")
    destination_folder = select_directory(title="Select Destination Folder")
    if not destination_folder:
        print("No destination folder selected. Exiting program.")
        sys.exit(1)

    return source_folder, destination_folder

# Function to ensure the destination folder exists
def check_destination_folder(destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

# List of all files in the source folder
def get_all_files(source_folder):
    return [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Function to display the number of files detected in the source folder
def display_file_count(source_folder):
    all_files = get_all_files(source_folder)
    print(f"\nDetected {len(all_files)} file(s) in the selected source folder.......")
    return all_files

# Define the copy or move function based on user input
def copy_or_move_file(file, batch_num, action, source_folder, destination_folder):
    batch_folder = os.path.join(destination_folder, f"Batch{batch_num}")
    if not os.path.exists(batch_folder):
        os.makedirs(batch_folder)

    # Construct source and destination paths
    source_file_path = os.path.join(source_folder, file)
    destination_file_path = os.path.join(batch_folder, file)

    # Perform the action: copy or move
    if action == 'c':
        shutil.copy2(source_file_path, destination_file_path)  # Copy the file
    elif action == 'm':
        shutil.move(source_file_path, destination_file_path)  # Move the file

# Function to handle the progress and spinning animation
def process_files(all_files, batch_size, action, source_folder, destination_folder):
    futures = []
    with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers for optimal performance
        for i, file in enumerate(all_files, 1):
            batch_num = (i - 1) // batch_size + 1  # Determine batch number based on file index
            futures.append(executor.submit(copy_or_move_file, file, batch_num, action, source_folder, destination_folder))

        # Display progress bar and spinner under it
        sys.stdout.write("\n")  # Move to the next line before starting the spinner.
        try:
            for i, future in enumerate(tqdm(futures, desc="Processing Files", unit="file", ncols=100, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} === {percentage:3.0f}%"), start=1):
                # Spinning wheel under the progress bar
                spinner = ['|', '/', '-', '\\']
                sys.stdout.write(f"\r{spinner[i % 4]}    ")  # Adding spaces to align the spinner
                sys.stdout.flush()
                time.sleep(0.1)  # Simulate time taken for file copy/move (adjust as needed)
                future.result()  # Block until each future (copy/move task) completes
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by user. Exiting...")
            sys.exit(1)

# Main function to guide the user and execute the script
def main():
    clear_screen()

    # Print out your name and copyright at the beginning
    print("File Organizer Tool")
    print("Developed by Pranav Kandakurthi")
    print("Copyright (c) 2025. All rights reserved.")
    print()

    # Select source and destination folders
    source_folder, destination_folder = select_folders()

    # Display the number of files in the source folder
    all_files = display_file_count(source_folder)
    
    if not all_files:
        print("No files found in the source folder. Exiting program.")
        return

    # Get user input for action (copy or move) and batch size
    action = get_action()
    batch_size = get_batch_size()

    # Check if the destination folder exists, if not, create it
    check_destination_folder(destination_folder)

    # Process files (copy or move them)
    print(f"\nStarting the process: {'Copying' if action == 'c' else 'Moving'} files in batches of {batch_size}...\n")
    process_files(all_files, batch_size, action, source_folder, destination_folder)

    # Provide feedback to the user after the process is complete
    print(f"\nAll files have been {'copied' if action == 'c' else 'moved'} into batches successfully!")

# Run the main function
if __name__ == "__main__":
    main()

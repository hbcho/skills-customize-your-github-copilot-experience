# 📘 Assignment: File Organization Automation

## 🎯 Objective

Build a Python script that organizes files into folders based on their file extensions. Practice using `pathlib`, functions, file operations, JSON data, and exception handling to automate a real-world task safely.

## 📝 Tasks

### 🛠️ Inspect the Source Folder

#### Description
Write a function that receives a folder path, checks whether the folder exists, and lists the files directly inside it. Ignore subfolders for this assignment.

#### Requirements
Completed program should:

- Use `pathlib.Path` to work with the folder and file paths
- Return or display the names of files in the source folder
- Handle a missing source folder with a clear error message instead of crashing


### 🛠️ Organize Files by Extension

#### Description
Create a destination folder for each file extension and move each file into the matching folder. For example, move `photo.jpg` to `organized/jpg/photo.jpg` and `notes.txt` to `organized/txt/notes.txt`.

#### Requirements
Completed program should:

- Create a folder named after each file extension when it does not already exist
- Move files with `Path.rename()` or `shutil.move()`
- Handle files without an extension by placing them in an `other` folder
- Avoid moving directories or files that are already inside the destination folder


### 🛠️ Save an Organization Log

#### Description
Record what the script did in a JSON file so that a user can review the results after the program finishes.

#### Requirements
Completed program should:

- Save a JSON log containing each moved file's original path, new path, and extension category
- Include a total count of moved files
- Handle permission or file-operation errors and continue when possible
- Print a short completion summary for the user

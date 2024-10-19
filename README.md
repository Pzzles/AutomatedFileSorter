Automated File Sorter Service

This project is a Python-based background service that monitors a folder (e.g., your Downloads folder) and automatically moves files into categorized folders on your desktop based on their file type. The service utilizes the watchdog library to detect file system changes and organize files for easier management.

Features
* Monitors the Downloads folder: Automatically detects new, modified, or moved files.
* File sorting based on type: Files are moved to specific folders on your desktop, categorized by their extensions:
 * Images for .jpg, .jpeg, .png, .gif
 *  Documents for .doc, .docx
 * PDFs for .pdf
 * Text files for .txt
 * Videos, Audio, Executables, and more based on extension
* Dynamic folder creation: New destination folders are created if they don’t already exist, ensuring files are always organized.
* Error handling: Incomplete downloads and temporary files (e.g., .crdownload, .part) are automatically filtered out.
* Performance optimization: Uses minimal system resources during idle periods.

Tech Stack
* Python
* watchdog library for monitoring file system events
* shutil for file moving operations

Prerequisites
* Python 3.10 or higher
* watchdog library

Install watchdog via pip:
pip install watchdog

Installation
1. Clone the repository: 
git clone https://github.com/Pzzles/AutomatedFileSorter.git
cd python-file-sorter
2. Run the script:
python SorterService.py

How It Works
The service monitors the Downloads folder using the watchdog library. When a file is created, modified, or moved, the service:

1. Determines the file's extension.
2. Moves the file into a corresponding folder on the desktop based on its type:
   * .txt files go to the TXT folder.
   * .pdf files go to the PDF folder.
   * Images like .jpg, .jpeg, and .png go to the Images folder.
   * .docx files go to the Documents folder.
   * Any unrecognized files are placed in the Others folder.

3. Creates folders dynamically if they don’t exist.
Configuration
 * The source folder being monitored is currently hardcoded as the Downloads folder (\Downloads).
 * The destination folders are automatically created on the desktop under appropriate categories (Images, PDFs, etc.).
 * These paths can be modified in the Watcher class, or you can pass them as arguments when initializing the service.

Customization
To handle additional file types:

 1. Open the SorterService.py file.
 2. Modify the category_mapping dictionary to include new file extensions and their corresponding folder names:
category_mapping = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi'],
    'Audio': ['.mp3', '.wav'],
    # Add more categories here
}

Creating an Executable (Optional)
To convert the Python script into an executable that can run in the background:
 1. Install PyInstaller:
pip install pyinstaller
2. Run the following command to generate the executable:
pyinstaller --noconsole --onefile SorterService.py

Error Handling
If an error occurs (such as a file being in use or permission issues), the service will log the error to the console and attempt retries for certain errors (like PermissionError). You can extend the error handling mechanism to log to a file for persistent storage.

Future Enhancements
 * Add more file type categories (e.g., archives, spreadsheets).
 * Allow monitoring of multiple directories.
 * Implement a configuration file for custom folder paths and categories.
 * Create a user-friendly UI for configuring file sorting preferences.

Contributing
If you'd like to contribute, please fork the repository and create a feature branch. Pull requests are welcome!









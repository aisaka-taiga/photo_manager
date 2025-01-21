RAW & JPG File Mover
This application is a simple file mover designed to organize RAW and JPG image files into separate folders. It allows users to drag and drop a folder or select a folder through a dialog. The application automatically sorts the files based on their extensions, moving RAW files to a "RAW" folder and JPG files to a "JPG" folder.

Features
Drag and drop functionality for easy folder selection.
Option to select a folder using a file dialog.
Automatically creates "RAW" and "JPG" folders if they do not exist.
Supports a wide range of RAW file formats from various camera manufacturers

Installation
```
git clone https://github.com/aisaka-taiga/photo_manager.git
```

```
cd photo_manager
```
Install the required packages:
```
pip install PySide6
```
Usage
Run the application using the following command:
```
python photo_manager.py
```
You can then drag and drop a folder containing your image files or select a folder using the "Select Folder" button. The application will sort the files into the appropriate folders.

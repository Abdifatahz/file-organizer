# Simple File Organizer Python Script

This Python script organizes files in a specified directory into subfolders based on their file types (extensions). 

## How It Works

1. The script lists all the files in the specified directory.
2. It checks the file extension of each file.
3. It creates a folder for each file type if it does not already exist.
4. It moves each file into its respective folder.

## Prerequisites

- Python 3.x
- The `os` and `shutil` modules (which are included in the Python standard library)

## Usage

1. Clone the repository or download the `organize.py` script.

    ```sh
    git clone https://github.com/Abdifatahz/file-organizer.git
    
    cd file-organizer
    ```

2. Run the script with the directory you want to organize as an argument.

    ```sh
    python organize.py <directory_path>
    ```
    
    Replace `<directory_path>` with the path to the directory you want to organize.

### Example

To organize files in the `Desktop` directory, run:

```sh
python organize.py ~/Desktop
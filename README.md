# Rename and Copy Chat Log JSON Files

This script processes a folder of `.json` files containing a `created_timestamp` field, copies the files into a subfolder, and renames them with the timestamp in the filename.

---

## Prerequisites

- **Python 3** must be installed on your Mac.  
  To check, open **Terminal** and run:
python3 --version

text
If Python 3 is missing, download and install it from [python.org](https://www.python.org/downloads/).

---

## Setup

1. Place `rename_copy_script.py` somewhere easy to access (like your Desktop).

2. Collect all your `.json` files into a single folder. For example:  
~/Desktop/my_json_logs


---

## Running the Script

1. Open **Terminal**.

2. Navigate to the folder where your script is located. Example if on Desktop:  
cd ~/Desktop


3. Run the script with the path to your JSON files folder:  
python3 rename_copy_script.py ~/Desktop/my_json_logs

*(Tip: You can drag the folder from Finder and drop it into Terminal after typing the script name to auto-fill the path.)*

---

## What the Script Does

- Scans **all `.json` files** in the specified folder.
- Copies each file into a new subfolder called `renamed_copies` within that folder.
- Renames the copied files to the format:  
YYYY-MM-DD_HH-MM_originalfilename.json

using the `created_timestamp` field to generate `YYYY-MM-DD_HH-MM`.
- Prints a sorted list of the original filenames with their human-readable timestamps.

---

## After Running

- Go into your JSON folder.
- Open the new subfolder `renamed_copies`.
- You will find copies of your files renamed with timestamps.

---

## Troubleshooting

- **Missing `created_timestamp` errors:**  
Make sure every JSON file includes a `created_timestamp` field.

- **Permission denied errors:**  
Check your folder permissions, or make the script executable:  
chmod +x rename_copy_script.py


- If any other errors occur, copy the Terminal error output and contact support for help.

---

Feel free to reach out if you need help or want additional features added!

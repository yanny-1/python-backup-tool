# Python Backup Tool

A Python script that copies files from source folders to backup folders based on configuration in `tasks.json`.

## Features
- Copies only files with specified extensions
- Preserves subfolder structure
- Checks if the file has been modified 
- Logs all operations in `log.txt`

## Requirements
- Python 3.x

## How to Run
1. Configure `tasks.json` with source and backup folders and file extensions.
2. Run the script:
```bash
python backup_script.py

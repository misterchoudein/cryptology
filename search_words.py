#!/usr/bin/env python3

import sys
import os
import glob

def find_in_files(files, keywords):
    """
    Search for each keyword in each file.
    Print file name, line number, and the keyword if found.
    """
    for file_path in files:
        # Safety check: skip directories or non-existent files
        if not os.path.isfile(file_path):
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_no, line in enumerate(f, start=1):
                    # Check each keyword
                    for kw in keywords:
                        if kw in line:
                            print(f"{file_path}:{line_no} -> {kw}")
        except Exception as e:
            print(f"Could not read {file_path}: {e}")

def gather_c_files(base_dir):
    """
    Recursively gather all *.c files from base_dir.
    """
    # Use glob to match recursively
    pattern = os.path.join(base_dir, '**', '*.c')
    return glob.glob(pattern, recursive=True)

def main():
    # 1. Capture arguments (excluding the script name)
    args = sys.argv[1:]
    
    # 2. If no arguments are given, gather all .c files in the current directory recursively
    if not args:
        files_to_search = gather_c_files('.')
    else:
        # Otherwise, treat each argument as a file or path to check
        # (If you expect directories, you can expand them here)
        files_to_search = []
        for arg in args:
            if os.path.isdir(arg):
                # If a directory was passed, gather .c files from it
                files_to_search.extend(gather_c_files(arg))
            else:
                # Otherwise assume it's a file
                files_to_search.append(arg)
    
    # 3. Define the keywords to look for
    keywords = ["TODO", "ADU"]
    
    # 4. Search
    find_in_files(files_to_search, keywords)

if __name__ == "__main__":
    main()

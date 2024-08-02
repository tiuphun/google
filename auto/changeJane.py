#!/usr/bin/env python3
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: python changeJane.py oldFiles.txt")
        sys.exit(1)

    old_files_path = sys.argv[1]

    try:
        with open(old_files_path, 'r') as file:
            old_files = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {old_files_path} does not exist.")
        sys.exit(1)

    for old_name in old_files:
        old_name = old_name.strip()
        new_name = old_name.replace('jane', 'jdoe')

        # Print debugging information
        print(f"Renaming: {old_name} -> {new_name}")

        try:
            subprocess.run(['mv', old_name, new_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error renaming file {old_name} to {new_name}: {e}")
            continue
    file.close()
if __name__ == "__main__":
    main()
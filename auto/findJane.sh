#!/bin/bash

# Define the path to list.txt
list_file="../data/list.txt"
data_dir="/home/student"       

# Create and empty oldFiles.txt in the scripts directory
touch oldFiles.txt
> oldFiles.txt

# Search for lines containing "jane" and save file names into an array
files=($(grep ' jane ' "$list_file" | awk '{print $3}'))

# Print the array for debugging
echo "Files array: ${files[@]}"

# Iterate over the array and append existing files to oldFiles.txt
for file in "${files[@]}"; do
    full_path="$data_dir$file"
    echo "Checking file: $full_path"
    if test -f "$full_path"; then
        echo "$full_path" >> oldFiles.txt
        echo "$full_path appended to oldFiles.txt"
    else
        echo "$full_path does not exist"
    fi
done
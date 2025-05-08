#!/bin/bash

REMOVE_ALL=false
REMOVE_EXISTING_ONLY=false

# Parse flags
while [[ "$1" =~ ^- ]]; do
    case "$1" in
        -r) REMOVE_ALL=true ;;
        -re) REMOVE_EXISTING_ONLY=true ;;
        *) echo "Unknown option: $1" ; exit 1 ;;
    esac
    shift
done

# Supported file extensions
EXTENSIONS=("ppt" "pptx" "doc" "docx")

# Find and convert files
for ext in "${EXTENSIONS[@]}"; do
    find . -type f -iname "*.${ext}" | while read -r file; do
        dir=$(dirname "$file")
        base=$(basename "$file")
        filename="${base%.*}"
        output_pdf="${dir}/${filename}.pdf"

        # Convert file using LibreOffice
        echo "Converting: $file"
        soffice --headless --convert-to pdf --outdir "$dir" "$file" >/dev/null 2>&1

        # Check if PDF was created
        if [[ -f "$output_pdf" ]]; then
            if $REMOVE_ALL; then
                echo "Removing original: $file"
                rm -f "$file"
            elif $REMOVE_EXISTING_ONLY; then
                echo "PDF exists, removing original: $file"
                rm -f "$file"
            fi
        else
            echo "❌ Failed to convert: $file"
        fi
    done
done


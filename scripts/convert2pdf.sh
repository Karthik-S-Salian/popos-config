#!/bin/bash

REMOVE_ALL=false
REMOVE_EXISTING_ONLY=false
TARGET_FILE=""

while [[ "$1" =~ ^- ]]; do
    case "$1" in
        -r)  REMOVE_ALL=true ;;
        -re) REMOVE_EXISTING_ONLY=true ;;
        *)   echo "Unknown option: $1" ; exit 1 ;;
    esac
    shift
done

# If a non-flag argument is left, treat it as a single file
if [[ $# -gt 0 ]]; then
    TARGET_FILE="$1"
fi

EXTENSIONS=("ppt" "pptx" "doc" "docx")

convert_file() {
    local file="$1"
    local dir base filename output_pdf
    dir=$(dirname "$file")
    base=$(basename "$file")
    filename="${base%.*}"
    output_pdf="${dir}/${filename}.pdf"

    echo "Converting: $file"
    soffice --headless --convert-to pdf --outdir "$dir" "$file" >/dev/null 2>&1

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
}

if [[ -n "$TARGET_FILE" ]]; then
    convert_file "$TARGET_FILE"
else
    for ext in "${EXTENSIONS[@]}"; do
        find . -type f -iname "*.${ext}" -print0 |
        while IFS= read -r -d '' file; do
            convert_file "$file"
        done
    done
fi


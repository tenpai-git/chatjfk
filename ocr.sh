#!/bin/bash

INPUT_DIR="jfk_pdfs"
OUTPUT_DIR="ocr_text"

mkdir -p "$OUTPUT_DIR"

for file in "$INPUT_DIR"/*.pdf; do
    base_name=$(basename "$file" .pdf)
    echo "Processing $file..."
    pdftoppm "$file" temp_image -png
    tesseract temp_image-1.png "$OUTPUT_DIR/$base_name" --oem 3 --psm 6
done

rm temp_image-*.png


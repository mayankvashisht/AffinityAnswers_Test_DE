#!/bin/bash

# Define the input URL
API_URL="https://www.amfiindia.com/spages/NAVAll.txt"

# Define the output TSV file
OUTPUT_FILE="output.tsv"

# Define the field names
FIELDS=("Scheme Name" "Net Asset Value")

# Initialize the output file with headers
echo "$(IFS=$'\t'; echo "${FIELDS[*]}")" > "$OUTPUT_FILE"

# Function to process and append data to the output file
function process_line {
    IFS=';' read -r -a fields <<< "$1"
    echo "${fields[3]}\t${fields[4]}" >> "$OUTPUT_FILE"
}

# Fetch data from the API and process it line by line
curl --location --request GET "$API_URL" | tail -n +3 | while read -r line; do
    process_line "$line"
done

echo "Conversion completed. Output saved to $OUTPUT_FILE"

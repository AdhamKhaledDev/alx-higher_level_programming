#!/bin/bash

# Check if URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Extract the URL from the argument
url="$1"

# Set the header value
header_name="X-School-User-Id"
header_value="98"

# Send GET request with header using curl
response=$(curl -s -H "$header_name: $header_value" "$url")

# Check if curl command was successful
if [ $? -eq 0 ]; then
  # Display the body of the response
  echo "$response"
else
  echo "Error: Failed to send GET request to $url"
  exit 1
fi

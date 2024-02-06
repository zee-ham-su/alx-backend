#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <flask_app_file>"
    exit 1
fi

# Set the FLASK_APP environment variable
export FLASK_APP="$1"

# Run Flask
flask run

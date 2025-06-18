#!/usr/bin/env python3
import sys

# Check if exactly one parameter is passed
if len(sys.argv) != 2:
    print("none")
else:
    # Get the string parameter
    input_string = sys.argv[1]

    # Check if the string contains the character 'z'
    if 'z' in input_string:
        # Print 'z' for each occurrence of 'z'
        print('z' * input_string.count('z'))
    else:
        print("none")

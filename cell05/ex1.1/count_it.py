#!/usr/bin/env python3
import sys

# Check if any parameters are passed
if len(sys.argv) <= 1:
    print("none")
else:
    # Display the number of parameters
    print(f"parameters: {len(sys.argv) - 1}")

    # Iterate over the parameters and print each one with its length
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
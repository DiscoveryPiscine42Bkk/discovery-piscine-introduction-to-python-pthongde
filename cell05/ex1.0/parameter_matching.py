#!/usr/bin/env python3
import sys

# Check the number of arguments passed
if len(sys.argv) != 2:
    print("none")
else:
    # Get the parameter passed in the command line
    parameter = sys.argv[1]

    # Prompt the user to enter a word
    user_input = input("What was the parameter? ")

    # Compare the user input with the parameter
    if user_input == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
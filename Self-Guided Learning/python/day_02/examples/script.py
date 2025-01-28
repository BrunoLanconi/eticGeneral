import os
import sys


# list_files() receives a directory path and lists all files in the directory. E.g. list_files("/home/user")
def list_files(directory):
    # NOTE Error handling will be covered in Day 09
    try:
        # Using os.listdir() to list all files in the directory
        files = os.listdir(directory)
        # For each file in the files list, print the file name
        for file in files:
            print(file)
    # This block will catch any exception that occurs in the try block
    except Exception as e:
        # Print the error message to stderr
        sys.stderr.write(f"Error: {e}\n")
        # Exit the script with a non-zero exit code (aka. failure)
        sys.exit(1)


# If the script is run directly, execute the list_files() function
# 'Run directly' means the script is executed using the python command. E.g. python script.py
if __name__ == "__main__":
    # If the number of arguments is not equal to 2, print the usage message and exit the script
    # An argument is the value passed to the script when it is executed. E.g. python script.py arg1
    if len(sys.argv) != 2:
        # list_files.py expects 1 argument, the directory path, but sys.argv will always have at least 1 element
        # sys.argv[0] is the script name, sys.argv[1] is the first argument, sys.argv[2] is the second argument, etc.
        sys.stderr.write("Usage: python list_files.py <directory_path>\n")
        sys.exit(1)

    directory_path = sys.argv[1]
    list_files(directory_path)

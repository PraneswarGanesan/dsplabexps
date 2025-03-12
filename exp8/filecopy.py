print("Enter the Name of Source File: ")
sourcefile = input()
print("Enter the Name of Target File: ")
targetfile = input()

try:
    # Open the source file for reading
    with open(sourcefile, "r") as fileHandle:
        texts = fileHandle.readlines()

    # Open the target file for writing
    with open(targetfile, "w") as fileHandle:
        for s in texts:
            fileHandle.write(s)

    print("File Copied Successfully!")
except FileNotFoundError:
    print("Error: The source file does not exist.")
except IOError:
    print("Error: An I/O error occurred.")

print("Enter the file to be opened")
sourcefile = input()
print("Enter the targetfile to be copied")
targetfile = input()
try:
    with open(sourcefile, "r") as fileHandle:
        text = fileHandle.readlines()

    with open(targetfile, "w") as fileHandle:
        for s in text:
            fileHandle.write(s)
    
    print("file copied succesfully")
except Exception as e:
    print(f"Error occured: {e}")
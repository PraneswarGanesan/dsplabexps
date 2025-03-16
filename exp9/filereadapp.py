def file_read(file_name):
    try:
        with open(file_name,'r') as file:
            cotent = file.read()
            print(f"file contents: {cotent}")
    except FileNotFoundError:
        print("Error:the file u mention is not exists")
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"An unexcepted error {e} occured")



file_read("readme.txt")
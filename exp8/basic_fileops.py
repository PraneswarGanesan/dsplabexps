# ============================
#  FILE CRUD OPERATIONS
# ============================

import os
import shutil

file_name = "sample.txt"
copy_file_name = "copy.txt"

# 1️⃣ Create or Write to a File (Overwrites if exists)
with open(file_name, "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python makes file handling easy.\n")
print(f"✅ '{file_name}' created and written.")

# 2️⃣ Read File Contents
with open(file_name, "r") as file:
    content = file.read()
print("\n🔹 File Content:\n", content)

# 3️⃣ Update (Append) File Contents
with open(file_name, "a") as file:
    file.write("This line is appended.\n")
print(f"✅ Data appended to '{file_name}'.")

# 4️⃣ Delete (Clear) File Contents
with open(file_name, "w") as file:
    file.truncate(0)  # Clears the file
print(f"✅ '{file_name}' is now empty.")

# 5️⃣ Copy File Contents to Another File
shutil.copy(file_name, copy_file_name)
print(f"✅ Contents of '{file_name}' copied to '{copy_file_name}'.")

# 6️⃣ Delete a File
delete_file = input("\nDo you want to delete 'sample.txt'? (yes/no): ")
if delete_file.lower() == "yes":
    os.remove(file_name)
    print("✅ File deleted.")
else:
    print("❌ File not deleted.")

# 7️⃣ Delete the Copied File
delete_copy = input("\nDo you want to delete 'copy.txt'? (yes/no): ")
if delete_copy.lower() == "yes":
    os.remove(copy_file_name)
    print("✅ Copied file deleted.")
else:
    print("❌ Copied file not deleted.")

print("\n🔷 END OF FILE CRUD OPERATIONS 🔷")

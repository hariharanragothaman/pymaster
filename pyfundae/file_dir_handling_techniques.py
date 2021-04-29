# To find out the current working directory
import os
import shutil

print("The current working directory is:", os.getcwd())

from pathlib import Path

print("The current working directory:", Path.cwd())

# Cleaning the workspace

shutil.rmtree(os.path.join(os.path.dirname(__file__), "artifact"))

# Create a new directory & checking if a directory is there or not?
os.mkdir("artifact")
print("Checking if the directory is there", os.path.exists("artifact"))

from pathlib import Path

Path("artifact").mkdir(parents=True, exist_ok=True)

# Remove a directory
# os.remove('artifact') - This will not work if there are no permissions and works only on files
shutil.rmtree(os.path.join(os.path.dirname(__file__), "artifact"))

# Zip and Unzip files
from zipfile import ZipFile

with ZipFile("text_files.zip", "w") as file:
    for txt_file in Path().glob("*.txt"):
        print(f"Add file :{txt_file.name} to the zip file")
        file.write(txt_file)

# Read files

# Read all the texts
with open("helloworld.txt", "r") as file:
    print(file.read())

# Read line by line
with open("helloworld.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"Reading line by line #{i}: {line}")

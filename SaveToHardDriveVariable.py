"""This program quickly moves files from one folder to another by file type"""
import os, shutil
from pathlib import Path

'''while True:
    sourceFolder = Path(input("Enter the source folder location: "))
    assert sourceFolder.exists()
    destinationFolder = Path(input("Enter the destination folder location: "))
    assert destinationFolder.exists()
    fileFormat = input("Choose file format (txt, jpg, pdf...): ").lower()
    for filename in os.listdir(sourceFolder):
        if filename.endswith(f".{fileFormat}"):
            if filename in os.listdir(destinationFolder):
                pass
            else:
                print(f"{filename} copied")
                shutil.copy(f"{sourceFolder}\\{filename}",
                            f"{destinationFolder}\\{filename}")
                print(f"{filename} moved to {destinationFolder}")
    break
print("\nAll files copied")'''

"""The version below will overwrite same-named files in the destination"""

while True:
    sourceFolder = Path(input("Enter the source folder location: "))
    assert sourceFolder.exists()
    destinationFolder = Path(input("Enter the destination folder location: "))
    assert destinationFolder.exists()
    fileFormat = input("Choose file format (txt, jpg, pdf...): ").lower()
    for filename in os.listdir(sourceFolder):
        if filename.endswith(f".{fileFormat}"):
            print(f"{filename} copied")
            shutil.copy(f"{sourceFolder}\\{filename}",
                        f"{destinationFolder}\\{filename}")
            print(f"{filename} moved to {destinationFolder}")
    break
print("\nAll files copied")

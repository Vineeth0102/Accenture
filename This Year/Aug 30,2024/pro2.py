"""
file version:

You're given a string array S That contains the name of some file along with their versions your task is to find and return an integer value representing the latest version out of all the files that are correctly named in the array a file is considered correct if it follows the format of the file name as "File_X" Var X represents the version of the file written one if there are no correct files in the array


"""

def version(files : list) -> int:
    version = 0
    for file in files:
        if file.startswith("File_"):
            filestr = file.split("_")
            if filestr[1].isdigit() and version < int(filestr[1]):
                version = int(filestr[1])
    return version


files = list(input().split())
print(version(files))



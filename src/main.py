"""main function of this directory, nothing really going on yet"""
import os
import shutil

def main():
    """main function"""
    source = "static/"
    destination = "public/"
    copy_to_destination(source, destination)

def copy_to_destination(source, destination):
    """function for copying directory and contents to new directory"""
    print(f"Copying directory tree {source} to {destination}")
    if not os.path.exists(source):
        raise ValueError(f"source not found: {source}")
    if not os.path.exists(destination):
        raise ValueError(f"destination not found: {destination}")
    print(f"Removing directory tree: {destination}")
    shutil.rmtree(destination)
    os.mkdir(destination)
    print("Starting recursive function")
    copy_to_destination_helper(source, destination)

def copy_to_destination_helper(source, destination):
    """function for copying directory and contents to new directory"""
    print(f"Current source: {source}")
    print(f"Current destination: {destination}")
    if not os.path.exists(source):
        raise ValueError(f"source not found: {source}")
    if not os.path.exists(destination):
        raise ValueError(f"destination not found: {destination}")
    contents = os.listdir(source)
    for i in contents:
        i_path = os.path.join(source, i)
        i_new = os.path.join(destination, i)
        if os.path.isfile(i_path):
            print(f"Copying file: {i_path}")
            shutil.copy(i_path, i_new)
            continue
        if os.path.isdir(i_path):
            print(f"Making directory: {i_new}")
            os.mkdir(i_new)
            copy_to_destination_helper(i_path, i_new)
            continue
        raise TypeError("object is neither file nor directory, so idk what's happening here")

if __name__ == "__main__":
    main()

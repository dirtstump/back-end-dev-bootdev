"""main function of this directory, nothing really going on yet"""
from website_functions import copy_to_destination

def main():
    """main function"""
    source = "static/"
    destination = "public/"
    copy_to_destination(source, destination)



if __name__ == "__main__":
    main()

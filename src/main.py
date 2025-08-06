"""main function of this directory, nothing really going on yet"""
import sys
from website_functions import (
    copy_to_destination,
    generate_to_destination,
)

def main():
    """main function"""
    basepath = sys.argv[1]
    if not basepath:
        basepath = "/"
    print(basepath)
    copy_source = "static/"
    generate_source = "content/"
    destination = "docs/"
    template = "template.html"
    copy_to_destination(copy_source, destination)
    generate_to_destination(generate_source, template, destination, basepath)


if __name__ == "__main__":
    main()

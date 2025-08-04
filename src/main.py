"""main function of this directory, nothing really going on yet"""
from website_functions import (
    copy_to_destination,
    generate_to_destination,
)

def main():
    """main function"""
    copy_source = "static/"
    generate_source = "content/"
    destination = "public/"
    template = "template.html"
    copy_to_destination(copy_source, destination)
    generate_to_destination(generate_source, template, destination)


if __name__ == "__main__":
    main()

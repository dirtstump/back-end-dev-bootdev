"""main function of this directory, nothing really going on yet"""
from website_functions import (
    copy_to_destination,
    generate_page,
)

def main():
    """main function"""
    source = "static/"
    destination = "public/"
    copy_to_destination(source, destination)
    generate_page("content/index.md", "template.html", "public/index.md")



if __name__ == "__main__":
    main()

"""functions for pulling together everything into a website"""
import os
import shutil
import re

from markdown_to_html import markdown_to_html_node

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

def extract_title(markdown):
    """extract the header (first line starting with "# ") from the markdown"""
    header = re.search(r"^# (.+)", markdown, re.MULTILINE)
    if not header:
        raise ValueError("error: No header")
    return header.group(1)

def generate_to_destination(source, template_path, destination, basepath):
    """function for copying directory and contents to new directory"""
    print(f"Generating from directory tree {source} to {destination}")
    if not os.path.exists(source):
        raise ValueError(f"source not found: {source}")
    if not os.path.exists(destination):
        raise ValueError(f"destination not found: {destination}")
    if not os.path.exists(template_path):
        raise ValueError(f"invalid 'template_path': {template_path}")
    if not os.path.isfile(template_path):
        raise ValueError(f"'template_path' must be a file: {template_path}")
    print("Starting recursive function")
    generate_to_destination_helper(source, template_path, destination, basepath)

def generate_to_destination_helper(source, template_path, destination, basepath):
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
            if not i_path.endswith(".md"):
                print(f"WARNING: Skipping non-'.md' file: {i_path}")
                continue
            i_new = i_new.replace(".md", ".html")
            print(f"Generating file: {i_path}")
            generate_page(i_path, template_path, i_new, basepath)
            continue
        if os.path.isdir(i_path):
            print(f"Making directory: {i_new}")
            os.mkdir(i_new)
            generate_to_destination_helper(i_path, template_path, i_new, basepath)
            continue
        raise TypeError("object is neither file nor directory, so idk what's happening here")

def generate_page(from_path, template_path, dest_path, basepath):
    """generate webpage from template and markdown"""
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # check for path validity
    if not os.path.exists(from_path):
        raise ValueError(f"invalid 'from_path': {from_path}")
    if not os.path.isfile(from_path):
        raise ValueError(f"'from_path' must be a file: {from_path}")

    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(template)

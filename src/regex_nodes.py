"""Functions for extracting image text and link text using regex"""
import re

def extract_markdown_images(text):
    """extract image text"""
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def extract_markdown_links(text):
    """extract link text"""
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

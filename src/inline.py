from enum import Enum
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    current = ""
    nodes = []
    open = False
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue
        for letter in node.text:
            if letter is delimiter:
                open = not open
            if not open:


    # for each node in old nodes
        # if node is not text type
            # error
        #for letters in text
            #when text is delimiter
                    # append TextNode(current, type)
                    # if text_type is text, 
                
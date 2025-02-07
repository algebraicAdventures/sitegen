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
        split_nodes = node.text.split(delimiter)
        if len(split_nodes) % 2 == 0:
            raise ValueError("Invalid markdown - delimiter not closed")
        for i in range(len(split_nodes)):
                nodes.append(TextNode(split_nodes[i], text_type))


    # for each node in old nodes
        # if node is not text type
            # error
        #for letters in text
            #when text is delimiter
                    # append TextNode(current, type)
                    # if text_type is text, 
                
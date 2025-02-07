import unittest
from inline import *

class TestInline(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [TextNode("Hello", TextType.TEXT), TextNode(" ", TextType.TEXT), TextNode("World", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(nodes, " ", TextType.TEXT), [TextNode("Hello", TextType.TEXT), TextNode("World", TextType.TEXT)])

if __name__ == "__main__":
    unittest.main()
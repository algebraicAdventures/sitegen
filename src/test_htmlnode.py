import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLNode("a", "Algebraic Art", None, {"href", "algebraicart.com"})
        node2 = HTMLNode("a", "Algebraic Art", None, {"href", "algebraicart.com"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLNode("a", "Algebraic Art", None, {"href": "algebraicart.com"})
        node2 = HTMLNode("a", "Algebraic Art", None, {"href": "algebraicart.com"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
    def test_ne1(self):
        node = HTMLNode("a", "Algebraic Art", None, None)
        node2 = HTMLNode("a", "Algebraic Art", None, {})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())
    def test_ne2(self):
        node = HTMLNode("a", "Algebraic Art", None, {"font-family": "algebraicart.com"})
        node2 = HTMLNode("a", "Algebraic Art", None, {"href": "algebraicart.com"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())
    def test_eq2(self):
        node = HTMLNode("a", "Algebraic Art", None, None)
        node2 = HTMLNode("a", "Algebraic Art", None, None)
        self.assertEqual(node.props_to_html(), node2.props_to_html())

class TestLeafNode(unittest.TestCase):
    def test_eq1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), node2.to_html())
    def test_ne1(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.bing.com"})
        self.assertNotEqual(node.to_html(), node2.to_html())

if __name__ == "__main__":
    unittest.main()
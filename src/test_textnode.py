import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Welcome to my portfolio!", TextType.ITALIC, "algebraicart.com")
        node2 = TextNode("Welcome to my portfolio!", TextType.ITALIC, "algebraicart.com")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Welcome to my portfolio!", TextType.ITALIC, "algebraicart.com")
        node2 = TextNode("Welcome to MY PORTFOLIO!", TextType.ITALIC, "algebraicart.com")
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("Welcome to my portfolio!", TextType.NORMAL, None)
        node2 = TextNode("Welcome to my portfolio!", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("Welcome to my portfolio!", TextType.ITALIC, "algebraicart.com")
        node2 = TextNode("Welcome to my portfolio!", TextType.LINK, "algebraicart.com")
        self.assertNotEqual(node, node2)

    def test_eq6(self):
        node = TextNode("Welcome to my portfolio!", TextType.NORMAL,)
        node2 = TextNode("Welcome to my portfolio!", TextType.NORMAL, "algebraicart.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
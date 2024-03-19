import unittest

from src.nodes.leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node3 = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(),  "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(),  "<a href=\"https://www.google.com\">Click me!</a>")
        self.assertEqual(node3.to_html(), "Click me!")

if __name__ == "__main__":
    unittest.main()
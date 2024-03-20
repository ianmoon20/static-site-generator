import unittest

from src.nodes.leafnode import LeafNode
from src.nodes.parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        parent_node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(parent_node.to_html(),  "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

        parent_node = ParentNode("div",
            [
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
            ],
        )

        self.assertEqual(parent_node.to_html(),  "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")

        parent_node = ParentNode("div",
            [
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
            ],
            {"href": "https://www.google.com"}
        )

        self.assertEqual(parent_node.to_html(),  "<div href=\"https://www.google.com\"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")

        parent_node = ParentNode("div",
            [
                ParentNode("div",
                    [
                        ParentNode("ol",
                            [
                                LeafNode("li", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("li", "italic text"),
                                LeafNode(None, "Normal text"),
                            ],
                        ),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
            ],
            {"href": "https://www.google.com"}
        )

        self.assertEqual(parent_node.to_html(),  "<div href=\"https://www.google.com\"><div><ol><li>Bold text</li>Normal text<li>italic text</li>Normal text</ol>Normal text<i>italic text</i>Normal text</div></div>")

if __name__ == "__main__":
    unittest.main()
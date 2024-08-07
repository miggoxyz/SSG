import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq_same_values(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_eq_different_values(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node1, node2)

    def test_eq_different_types(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("Link", "link", "https://example.com")
        node2 = TextNode("Link", "link", "https://example.com")
        self.assertEqual(node1, node2)

    def test_eq_different_url(self):
        node1 = TextNode("Link", "link", "https://example.com")
        node2 = TextNode("Link", "link", "https://different.com")
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Test", "bold", "https://example.com")
        expected_repr = "TextNode(Test, bold, https://example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_text_property(self):
        node = TextNode("Test text", "plain")
        self.assertEqual(node.text, "Test text")

    def test_text_type_property(self):
        node = TextNode("Test text", "italic")
        self.assertEqual(node.text_type, "italic")

    def test_url_property(self):
        node = TextNode("Link", "link", "https://example.com")
        self.assertEqual(node.url, "https://example.com")

    def test_url_default_value(self):
        node = TextNode("Test text", "plain")
        self.assertIsNone(node.url)


if __name__ == '__main__':
    unittest.main()

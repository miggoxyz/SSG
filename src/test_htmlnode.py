import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init_with_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_values(self):
        node = HTMLNode("div", "Hello", [
                        "child1", "child2"], {"class": "test"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, ["child1", "child2"])
        self.assertEqual(node.props, {"class": "test"})

    def test_to_html_raises_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"class": "test"})
        self.assertEqual(node.props_to_html(), 'class="test"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"class": "test", "id": "main"})
        self.assertIn(node.props_to_html(), [
                      'class="test" id="main"', 'id="main" class="test"'])

    def test_repr(self):
        node = HTMLNode("div", "Hello", [
                        "child1", "child2"], {"class": "test"})
        expected_repr = "HTMLNode(div, Hello, ['child1', 'child2'], {'class': 'test'})"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_with_defaults(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(node), expected_repr)


if __name__ == '__main__':
    unittest.main()

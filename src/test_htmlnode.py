import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(None, None, None, {"test":"case"})
        self.assertEqual(node1.props_to_html(), ' test="case"')

    def test_props_to_html_none(self):
        node1 = HTMLNode(None, None, None, None)
        self.assertEqual(node1.props_to_html(), "")

    def test_props_to_html_multiple(self):
        node1 = HTMLNode(None, None, None, {"test1":"case1", "test2":"case2"})
        self.assertEqual(node1.props_to_html(), ' test1="case1" test2="case2"')
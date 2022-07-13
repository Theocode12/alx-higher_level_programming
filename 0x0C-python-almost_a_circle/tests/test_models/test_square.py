#!/usr/bin/python3
"""
Test cases for Square class
"""

import unittest
import json
import inspect
import pep8
import os
from unittest.mock import patch
from io import StringIO
from models import square

Square = square.Square

class TestSquareDocs(unittest.TestCase):
    """
    Testing if docs are present and if the files are PEP valid
    """

    def test_Square_pep8_conformance(self):
        """Test if Square conforms to pep8 style"""

        pep_check = pep8.StyleGuide()
        result = pep_check.check_files(["models/square.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docs(self):
        """checks if module documentation is present"""

        self.assertTrue(len(square.__doc__) > 4)

    def test_cls_docs(self):
        """checks if class docs are present"""

        self.assertTrue(len(Square.__doc__) > 4)

    def test_method_docs(self):
        """checks if method documentation are present"""

        methods = inspect.getmembers(Square, inspect.isfunction)
        for method in methods:
            method = Square.__name__ + '.' + method[0]
            self.assertTrue(len(eval(method).__doc__) > 4)

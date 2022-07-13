#!/usr/bin/python3
from models import square
import unittest
import json
import inspect
import pep8
import os
from unittest.mock import patch
from io import StringIO


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

class TestSquare(unittest.TestCase):
    """check that Squares functionality"""

    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(1)
        cls.s2 = Square(3, 1, 1)
        cls.s3 = Square(6, 1, 1, 1)
        
    
    def test_object_id(self):
        """test object id"""

        self.assertEqual(self.s1.id, 24)
        self.assertEqual(self.s2.id, 25)
        self.assertEqual(self.s3.id, 1)
    
    def test_width(self):
        self.assertEqual(self.s1.width, 14)
        self.assertEqual(self.s2.width, 3)
        self.assertEqual(self.s3.width, 6)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 3)
        self.assertEqual(self.s3.height, 6)

    def test_size_getter(self):
        """Test size property"""

        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 3)
        self.assertEqual(self.s3.size, 6)
    
    def test_size_setter(self):
        """Test size setter."""

        self.s1.size = 14
        self.assertEqual(self.s1.size, 14)

    def test_size_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.s1.size = None
        with self.assertRaises(TypeError):
            Square(None, 13)

    def test_size_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.s2.size = "13"
        with self.assertRaises(TypeError):
            Square("hello", 13)

    def test_size_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.s2.size = -3
        with self.assertRaises(ValueError):
            Square(-3, 4)


    def test_when_required_args_not_passed(self):
        with self.assertRaises(TypeError):
            Square()

    def test_x_setter(self):
        """Test x setter."""

        self.s3.x = 14
        self.assertEqual(self.s3.x, 14)

    def test_x_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.s3.x = None
        with self.assertRaises(TypeError):
            Square(3, None)


    def test_x_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.s2.x = "13"
        with self.assertRaises(TypeError):
            Square(3, "4", 4)

    def test_x_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.s3.x = -10
        with self.assertRaises(ValueError):
            Square(3, -10, -2)


    def test_y_setter(self):
        """Test y setter."""

        self.s1.y = 3
        self.assertEqual(self.s1.y, 3)


    def test_y_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.s1.y = None
        with self.assertRaises(TypeError):
            Square(2, 3, None)

    def test_y_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.s1.y = "13"
        with self.assertRaises(TypeError):
            Square(3, 4, "5")

    def test_y_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.s3.y = -10
        with self.assertRaises(ValueError):
            Square(3, 2, -3)

    def test_area(self):
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 9)
        self.assertEqual(self.s3.area(), 36)

    def test_area_with_value_passed(self):
        with self.assertRaises(TypeError):
            self.s1.area(6)

    def test_str_methods(self):
        self.assertEqual(str(self.s1), '[Square] (24) 0/0 - 14')
        self.assertEqual(str(self.s2), '[Square] (25) 1/1 - 3')
        self.assertEqual(str(self.s3), '[Square] (1) 1/1 - 6')

    def test_update_method_using_args(self):
        r = Square(1, 1)
        r.update(10)
        self.assertEqual(str(r), '[Square] (10) 1/0 - 1')
        r.update(10, 3)
        self.assertEqual(str(r), '[Square] (10) 1/0 - 3')
        r.update(10, 3, 5)
        self.assertEqual(str(r), '[Square] (10) 5/0 - 3')
        r.update(10, 3, 5, 2)
        self.assertEqual(str(r), '[Square] (10) 5/2 - 3')
        r.update(10, 3, 5, 2, 1)
        self.assertEqual(str(r), '[Square] (10) 5/2 - 3')

    def test_udate_method_using_kwargs(self):
        r = Square(1, 1)
        r.update(**{"id":4, "size":3, "x":4, "y":4})
        self.assertEqual(str(r), '[Square] (4) 4/4 - 3')

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Square(1, 1, 0, 1)
        r.update(1, 1, 1, 1, 2)
        self.assertEqual(str(r), '[Square] (1) 1/1 - 1')

    def test_update_no_args(self):
        """test no args for update"""
        r = Square(1, 1, 0, 1)
        r.update()
        self.assertEqual(str(r), '[Square] (1) 1/0 - 1' )

    def test_mix_args_kwargs(self):
        """tests output for mixed args and kwargs"""
        r = Square(1, 1, 0, 1)
        r.update(2, 2, 2, 2, 2, size=3, x=3, y=3, id=3)
        self.assertEqual(str(r), '[Square] (2) 2/2 - 2')

    def test_to_dictionary(self):
        r_1 = Square(1, 1, id=3)
        self.assertDictEqual(r_1.to_dictionary(), {"id": 3, "size": 1, "x": 1, "y": 0})
        r_1 = Square(1, 1, 3, 6)
        self.assertDictEqual(r_1.to_dictionary(), {'id': 6, 'size': 1, 'x': 1, 'y': 3})
        self.assertIs(type(r_1.to_dictionary()), dict)

    def test_save_to_file(self):
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        l = [s1, s2]
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            ls = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_create_class_method(self):
        d1 = {"id": 3, "size": 1, "x": 0, "y": 0}
        d2 = {"id": 9, "size": 3, "x": 3, "y": 0}
        r_1 = Square.create(**d1)
        r_2 = Square.create(**d2)
        self.assertEqual(str(r_1), "[Square] (3) 0/0 - 1")
        self.assertEqual(str(r_2), "[Square] (9) 3/0 - 3")
        self.assertIsNot(r_1, r_2)
        self.assertNotEqual(r_1, r_2)
        self.assertIs(type(r_1), type(r_2))

    def test_load_from_file_if_not_present(self):
        try:
            os.remove("Square.json")
        except Exception:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file(self):
        r_1 = Square(4, 1, 4, 2)
        r_2 = Square(3, 2, 2, 2)
        ls = [r_1, r_2]
        Square.save_to_file(ls)
        nw_ls = Square.load_from_file()
        self.assertIs(type(nw_ls), list)
        self.assertIs(type(nw_ls[0]), Square)
        self.assertEqual(len(nw_ls), 2)
        self.assertEqual(str(nw_ls[0]), str(r_1))
        self.assertIsNot(nw_ls[0], ls[0])


    def test_basic_display(self):
        
        r = Square(2)
        expected_display = "##\n##\n"
        with patch('sys.stdout', new = StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected_display)


    def test_display_xy(self):
        """Testing the display method with x and y"""
        r = Square(2, 2, 2, 2)
        expected_display = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new = StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected_display)

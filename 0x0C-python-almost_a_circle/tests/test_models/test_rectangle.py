"""
Test cases for Rectangle class
"""


from models import rectangle
import unittest
import json
import inspect
import pep8
import os
from unittest.mock import patch
from io import StringIO

Rectangle = rectangle.Rectangle

class TestRectangleDocs(unittest.TestCase):
    """
    Testing if docs are present and if the files are PEP valid
    """

    def test_rectangle_pep8_conformance(self):
        """Test if rectangle conforms to pep8 style"""

        pep_check = pep8.StyleGuide()
        result = pep_check.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docs(self):
        """checks if module documentation is present"""

        self.assertTrue(len(rectangle.__doc__) > 4)

    def test_cls_docs(self):
        """checks if class docs are present"""

        self.assertTrue(len(Rectangle.__doc__) > 4)

    def test_method_docs(self):
        """checks if method documentation are present"""

        methods = inspect.getmembers(Rectangle, inspect.isfunction)
        for method in methods:
            method = Rectangle.__name__ + '.' + method[0]
            self.assertTrue(len(eval(method).__doc__) > 4)

class TestRectangle(unittest.TestCase):
    """check that rectangles functionality"""

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(1, 1)
        cls.r2 = Rectangle(3, 1, 1)
        cls.r3 = Rectangle(6, 1, 1, 1)
        cls.r4 = Rectangle(9, 1, 1, 1, 10)
    
    def test_object_id(self):
        """test object id"""

        self.assertEqual(self.r1.id, 12)
        self.assertEqual(self.r2.id, 13)
        self.assertEqual(self.r3.id, 14)
        self.assertEqual(self.r4.id, 10)
    
    def test_width_getter(self):
        """Test width property"""

        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r3.width, 6)
        self.assertEqual(self.r4.width, 9)
    
    def test_width_and_height(self):
        r_1 = Rectangle(1, 2)
        self.assertIs(type(r_1), Rectangle)


    def test_width_setter(self):
        """Test width setter."""

        self.r1.width = 14
        self.assertEqual(self.r1.width, 14)

    def test_width_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.r1.width = None
        with self.assertRaises(TypeError):
            Rectangle(None, 13)

    def test_width_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.r2.width = "13"
        with self.assertRaises(TypeError):
            Rectangle("hello", 13)

    def test_width_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.r2.width = -3
        with self.assertRaises(ValueError):
            Rectangle(-3, 4)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_setter(self):
        """Test height setter."""

        self.r4.height = 14
        self.assertEqual(self.r4.height, 14)

    def test_height_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.r4.height = None
        with self.assertRaises(TypeError):
            Rectangle(4, None)

    def test_height_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.r2.height = "13"
        with self.assertRaises(TypeError):
            rectangle(4, "world")

    def test_when_width_and_height_is_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_width_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.r4.height = -10
        with self.assertRaises(ValueError):
            Rectangle(10, -10)

    def test_when_required_args_not_passed(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(12)

    def test_x_setter(self):
        """Test x setter."""

        self.r3.x = 14
        self.assertEqual(self.r3.x, 14)

    def test_x_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.r3.x = None
        with self.assertRaises(TypeError):
            Rectangle(3, 5, None)


    def test_x_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.r2.x = "13"
        with self.assertRaises(TypeError):
            Rectangle(3, 3, "4", 4)

    def test_x_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.r4.x = -10
        with self.assertRaises(ValueError):
            Rectangle(3, 5, -10)


    def test_y_setter(self):
        """Test y setter."""

        self.r1.y = 3
        self.assertEqual(self.r1.y, 3)


    def test_y_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            self.r1.y = None
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 5, None)

    def test_y_setter_when_type_wrong(self):
        """test setter when wrong type is passed"""

        with self.assertRaises(TypeError):
            self.r1.y = "13"
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 1, "5")

    def test_y_when_neg_num_passed(self):
        """test setter when negative number is passed"""

        with self.assertRaises(ValueError):
            self.r4.y = -10
        with self.assertRaises(ValueError):
            Rectangle(3, 2, 2, -3)

    def test_area(self):
        self.assertEqual(self.r1.area(), 1)
        self.assertEqual(self.r2.area(), 3)
        self.assertEqual(self.r3.area(), 6)
        self.assertEqual(self.r4.area(), 9)

    def test_area_with_value_passed(self):
        with self.assertRaises(TypeError):
            self.r1.area(6)

    def test_str_methods(self):
        self.assertEqual(str(self.r1), "[Rectangle] (12) 0/0 - 1/1")
        self.assertEqual(str(self.r2), "[Rectangle] (13) 1/0 - 3/1")
        self.assertEqual(str(self.r3), "[Rectangle] (14) 1/1 - 6/1")
        self.assertEqual(str(self.r4), "[Rectangle] (10) 1/1 - 9/14")

    def test_update_method_using_args(self):
        r = Rectangle(1, 1)
        r.update(10)
        self.assertEqual(str(r), "[Rectangle] (10) 0/0 - 1/1")
        r.update(10, 3)
        self.assertEqual(str(r), "[Rectangle] (10) 0/0 - 3/1")
        r.update(10, 3, 5)
        self.assertEqual(str(r), "[Rectangle] (10) 0/0 - 3/5")
        r.update(10, 3, 5, 2)
        self.assertEqual(str(r), "[Rectangle] (10) 2/0 - 3/5")
        r.update(10, 3, 5, 2, 1)
        self.assertEqual(str(r), "[Rectangle] (10) 2/1 - 3/5")

    def test_udate_method_using_kwargs(self):
        r = Rectangle(1, 1)
        r.update(**{"id":4, "width":3, "height":2, "x":4, "y":4})
        self.assertEqual(str(r), "[Rectangle] (4) 4/4 - 3/2")

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_mix_args_kwargs(self):
        """tests output for mixed args and kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_to_dictionary(self):
        r_1 = Rectangle(1, 1, id=3)
        self.assertDictEqual(r_1.to_dictionary(), {"id": 3, "width": 1, "height": 1, "x": 0, "y": 0})
        r_1 = Rectangle(1, 1, 3, 4, 6)
        self.assertDictEqual(r_1.to_dictionary(), {"id": 6, "width": 1, "height": 1, "x": 3, "y": 4})
        self.assertIs(type(r_1.to_dictionary()), dict)

    def test_save_to_file(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_create_class_method(self):
        d1 = {"id": 3, "width": 1, "height": 1, "x": 0, "y": 0}
        d2 = {"id": 9, "width": 3, "height": 5, "x": 3, "y": 0}
        r_1 = Rectangle.create(**d1)
        r_2 = Rectangle.create(**d2)
        self.assertEqual(str(r_1), "[Rectangle] (3) 0/0 - 1/1")
        self.assertEqual(str(r_2), "[Rectangle] (9) 3/0 - 3/5")
        self.assertIsNot(r_1, r_2)
        self.assertNotEqual(r_1, r_2)
        self.assertIs(type(r_1), type(r_2))

    def test_load_from_file_if_not_present(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        r_1 = Rectangle(4, 1, 4, 2)
        r_2 = Rectangle(3, 2, 2, 2)
        ls = [r_1, r_2]
        Rectangle.save_to_file(ls)
        nw_ls = Rectangle.load_from_file()
        self.assertIs(type(nw_ls), list)
        self.assertIs(type(nw_ls[0]), Rectangle)
        self.assertEqual(len(nw_ls), 2)
        self.assertEqual(str(nw_ls[0]), str(r_1))
        self.assertIsNot(nw_ls[0], ls[0])


    def test_basic_display(self):
        
        r = Rectangle(2, 3, 0, 0, 1)
        expected_display = "##\n##\n##\n"
        with patch('sys.stdout', new = StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected_display)


    def test_display_xy(self):
        """Testing the display method with x and y"""
        r = Rectangle(2, 2, 2, 2, 1)
        expected_display = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new = StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected_display)

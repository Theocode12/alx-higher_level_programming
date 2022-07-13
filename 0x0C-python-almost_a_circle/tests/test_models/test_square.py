#!/usr/bin/python3
import unittest
import json
import inspect
import pep8
import os
from unittest.mock import patch
from io import StringIO
from models import square

Square = square.Square
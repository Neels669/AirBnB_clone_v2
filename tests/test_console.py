#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
        """Unittests for testing the HBNB command interpreter."""

        @classmethod
        def setUpClass(cls):
            """HBNBCommand testing setup."""
            try:
                os.rename("file.json", "tmp")
            except IOError:
                pass

            cls.HBNB = HBNBCommand()

        @classmethod
        def tearDownClass(cls):
            """HBNBCommand testing teardown."""
            try:
                os.rename("tmp", "file.json")
            except IOError:
                pass
            del cls.HBNB

        def setUp(self):
                """Reset FileStorage objects dictionary."""
                FileStorage._FileStorage__objects = {}

        def tearDown(self):
            """Delete any created file.json."""
            try:
                os.remove("file.json")
            except IOError:
                pass


    if __name__ == "__main__":
        unittest.main()


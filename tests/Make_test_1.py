# Unit Test 1: File Existence Check

import sys
import os.path
from tud_tests import *

def test_file_exists():
    try:
        exists = os.path.exists("./Make.py")
        assert exists == True, "Make.py file does not exist."
    except AssertionError as e:
        sys.exit(str(e))

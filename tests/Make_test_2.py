# Unit Test 2: Input Validation for Option Selection

import sys
from tud_tests import *
sys.path.append(".")

def test_input_validation():
    set_keyboard_input(["4", "-1", "abc", "2"])  # Invalid inputs followed by a valid input
    import Make
    output = get_display_output()
    
    expected_prompts = [
        "Choose an option: (1) Output range, (2) From point to end, (3) From beginning to point",
        "Please enter a valid option (1, 2, or 3):"
    ]
    assert expected_prompts[1] in output, "Invalid input handling not implemented correctly."

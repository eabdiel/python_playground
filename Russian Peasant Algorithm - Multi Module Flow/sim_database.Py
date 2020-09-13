"""
Simulation of Web App Architecture | Case study based on assignment from
                                                https://www.udemy.com/share/103nlaAEMZdllWTHg=/
Run flow_controller.py to start
"""
import time


def russian(a, b):
    x = a;
    y = b  # Semicolon -> Compound Statement
    z = 0  # Acumulator
    while x > 0:  # While Loop Begins
        if x % 2 == 1: z = z + y  # Modulo operator
        y = y << 1  # Shift Binary over to left
        x = x >> 1  # Shift Binary over to right
    print("/////////////////////////////")
    print("**********Hit DB*************")
    print("/////////////////////////////")
    return z  ## Return Z


def test_russian():
    start_time = time.time()
    print(russian(357, 16))
    print("Russian Algorithm took %f seconds" % (time.time() - start_time))
    assert russian(357, 16) == 5712


if __name__ == "__main__":
    test_russian()
# End of code - github.com/eabdiel

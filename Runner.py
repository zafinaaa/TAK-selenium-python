import unittest
from unittest.suite import TestSuite
import register_user, login_user, add_to_cart

if __name__ == "__main__":
    # create test suite from classes
    suite = TestSuite()

    # call test
    tests = unittest.TestLoader()

    # add test to suite
    suite.addTest(tests.loadTestsFromModule(register_user))
    suite.addTest(tests.loadTestsFromModule(login_user))
    suite.addTest(tests.loadTestsFromModule(add_to_cart))

    # run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
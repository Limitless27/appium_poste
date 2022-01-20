import unittest
from unittest import TestCase

from method_object import Methods

class Test(TestCase):

    def test_1(self):
        try:
            methods = Methods()
            print(methods.desired_cap)
            desired = methods.details()
            methods.AppiumServiceStart(desired)
            methods.appium_service.stop()
        except:
            print()
    def test_2(self):
        try:
            methods = Methods()
            print(methods.desired_cap)
            desired = methods.details()
            methods.AppiumServiceStart(desired)
            methods.appium_service.stop()
        except:
            print()

if __name__ == '__main__':
    unittest.main()
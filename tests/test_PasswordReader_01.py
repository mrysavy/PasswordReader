import unittest
from passwordreader.PasswordReader import *
from passwordreader.Modules import ValueModule


class PasswordReaderTestCase(unittest.TestCase):

    def testValueModule(self):
        self.assertEqual(
            readPassword(ValueModule("VALUE1")),
            "VALUE1",
            "ValueModule")


if __name__ == "__main__":
    unittest.main()

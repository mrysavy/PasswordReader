import unittest
from cz.rysavi.PasswordReader.PasswordReader import *
from cz.rysavi.PasswordReader.Modules import ValueModule


class PasswordReaderTestCase(unittest.TestCase):

    def testValueModule(self):
        self.assertEqual(
            readPassword(ValueModule("VALUE1")),
            "VALUE1",
            "ValueModule")


if __name__ == "__main__":
    unittest.main()

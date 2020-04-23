import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")
     
    # @unittest.skip("WIP") # Work In Progress
    def test_empty_phonebook_is_consistent(self):
        phonebook = PhoneBook()
        self.assertTrue(phonebook.is_consistent())

    def test_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "12345")
        self.assertTrue(self.phonebook.is_consistent()
        self.phonebook.add("Sue", "123")
        self.assertTrue(self.phonebook.is_consistent())

     



# Run in terminal using command "python -m unittest"
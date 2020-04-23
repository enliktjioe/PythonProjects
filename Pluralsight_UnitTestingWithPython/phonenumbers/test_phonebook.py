import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)

# Run in terminal using command "python -m unittest"
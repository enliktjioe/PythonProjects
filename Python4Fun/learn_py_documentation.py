# Reference: 
# https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings

# def say_hello(name):
#     print(f"Hello {name}, is it me you're looking for?")

# say_hello.__doc__ = "A simple function that says hello... Richie style"


# help(say_hello)

class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(f'Hello {name}')

    help(say_hello)

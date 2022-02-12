# Class
class Human:
    pass


# Object creation
# When we need to call same object multiple times.
male = Human()
female = Human()

# In case of single time use
Human()


# Methods
class Human:
    def walk(self):
        pass


# Inheritance
class Human:
    def walk(self):
        print('Walking...')


class Male(Human):
    def walk(self):
        print('Walking...')


Male().walk()


# Abstraction
class Male:
    # Class variable
    ADDRESS = "India"

    @classmethod
    def update_address(cls, new_address):
        cls.ADDRESS = new_address


Male.update_address("USA")
print(Male.ADDRESS)


# Encapsulation
class Male:
    # Class variable
    __ADDRESS = "India"

    @classmethod
    def update_address(cls, new_address):
        cls.__ADDRESS = new_address

    @classmethod
    def get_address(cls):
        return cls.__ADDRESS


Male.update_address("USA")
print(Male.get_address())


# Polymorphism
class Male:
    def get_type(self):
        print('Male Type')


class Female:
    def get_type(self):
        print('Female Type')


def get_type(object):
    object.get_type()


get_type(Male())
get_type(Female())

#!/usr/bin/python3
""" Define a student class """


class Student():
    """ Represent a student """

    def __init__(self, first_name, last_name, age):
        """ Initialize a student.

        Args:
        first_name (str): first name of astudent
        last_name (str): last name of a student
        age (int): age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary representation of a student """
        return self.__dict__

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:45:15 2016

@author: dell
"""

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        self.status = status
        if self.status.lower() != "citizen" and self.status.lower() != "legal_resident" and self.status.lower() != "illegal_resident":
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        if self.status.lower() != "citizen" and self.status.lower() != "legal_resident" and self.status.lower() != "illegal_resident":
            raise ValueError
        else:        
            return self.status


barry = USResident("barry", "citizen")
tom = USResident("tom", "legal_resident")
dave = USResident("dave", "illegal_resident")
john = USResident("john", "LEGAL_resident")
tim = USResident("tim", "citizeN")
glynn = USResident("glynn", "CITIZEN")
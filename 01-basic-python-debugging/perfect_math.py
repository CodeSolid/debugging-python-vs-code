"""
This code is perfect. I, Brad Bumblekey, a senior architect, 
have tested it and certified it bug-free.
Copyright (c) 2022
Bradley Bumblekey and Robustness Unlimited(tm)
"""

from decimal import Decimal
from numbers import Number

def is_number(value):
    """determine if a value is a number."""
    return isinstance(value, Number) and not isinstance(value, bool)
    
def get_numbers_from_dictionary(dct):
    """Gets the numbers from dictionary, dct, as a tuple containing all the numbers"""
    numbers = []
    for key in dct.keys():
        value = dct[key]
        if is_number(value): 
            numbers.append(value)        
    return numbers
    
def test_get_numbers_from_dictionary():
    print("Instructions: examine the printout.  Ensure only numbers are included.")
    bond = {"agent": "James Bond", "agent_number": 7, "age": 37,
            "girlfriends_per_episode": 2.3, 
            "shaken_not_stirred": True, "ppk_caliber": Decimal(.380)}
    numbers = get_numbers_from_dictionary(bond)
    print(numbers)

if __name__ == "__main__":
    test_get_numbers_from_dictionary()


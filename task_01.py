#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


import pet


class Dog(pet.Pet):
    """A Dog is a subclass of the Pet class."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the Dog() sub-class.

        Args:
            has_shots (boolean, optional): Verifies the dog has their shots.
            Defaults to False.
            **kwargs (dictionary): An arbitrary arguments dictionary.

        Attributes:
            has_shots (boolean): Verifies the dog has their shots.
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)

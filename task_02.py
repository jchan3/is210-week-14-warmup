#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """A function that returns a dictionary of the fruit items and total cost
        per-item.

    Args:
        shoplist (dictionary): A dictionary with a key of fruit items and values
        of integers indicating the number of units to purchase.

    Returns:
        dictionary: A dictionary keyed by the name of the fruit with the total
        cost per-item reflected.

    Examples:
        >>> shoplist = {'Lime':12,'Red Pear': 4, 'Peach': 24}
        >>> get_cost_per_item(shoplist)
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {key: FRUIT[key]*value for key, value in shoplist.iteritems()
            if key in FRUIT}


def get_total_cost(shoplist):
    """A function that returns the total cost of all the fruit items in
        shoplist.

    Args:
        shoplist (dictionary): A dictionary with a key of fruit items and values
        of integers indicating the number of units to purchase.

    Returns:
        float: The sum of the values in the dictionary created by
        get_cost_per_item().

    Examples:
        >>> shoplist = {'Lime':12,'Red Pear': 4, 'Peach': 24}
        >>> get_total_cost(shoplist)
        112.80000000000001
    """
    return sum([value for value in get_cost_per_item(shoplist).itervalues()])

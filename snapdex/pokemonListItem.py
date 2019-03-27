# -*- coding: utf-8 -*-
""" PokemonListItem class """
import random


MISSINGNO_SPRITE = 'https://cdn.bulbagarden.net/upload/9/98/Missingno_RB.png'


class PokemonListItem(object):
    """
    Represents a Pokemon's entry in the list of Pokemon the bot supports
    """

    def __init__(self, name, alias_list=None, number=0, types=None,
                 dex_entries=None, sprite=None, legendary=False, mythic=False,
                 regional=False):
        """
        Create the Pokemon List Item

        :param name: Name of the Pokemon (same as Pokemon Go)
        :type name: basestring
        :param alias_list: A list of alias names (i.e. Mr Mime, Mr. Mime)
        :type alias_list: basestring[]
        :param number: Number of the Pokemon in the Pokemon Go dex
        :type number: int
        :param types: Types the Pokemon has
        :type types: basestring[]
        :param dex_entries: Dex Entries through the generations
        :type dex_entries: basestring[]
        :param sprite: URL for a sprite
        :type sprite: basestring
        :param legendary: Is the Pokemon legendary Pokemon?
        :type legendary: bool
        :param mythic: Is the Pokemon a mythic Pokemon?
        :type mythic: bool
        :param regional: Is the Pokemon a regional Pokemon?
        :type regional: bool
        """
        if not name:
            raise Exception('No name provided')
        self.name = name
        self.alias_list = alias_list if alias_list else []
        self.number = number
        self.types = types if types else []
        self.dex_entries = dex_entries if dex_entries else []
        self.sprite = sprite if sprite else MISSINGNO_SPRITE
        self.legendary = legendary
        self.mythic = mythic
        self.regional = regional

    def get_name_search_list(self):
        """
        Get the list of names to match for this Pokemon

        :return: List of names
        :rtype: basestring[]
        """
        return [self.name.lower()] + [name.lower() for name in self.alias_list]

    def get_types(self):
        """
        Get the type combination (if applicable) for the Pokemon

        :return: Type(s) for the Pokemon
        :rtype: basestring
        """
        return "/".join(self.types)

    def get_dex_entry(self):
        """
        Get a random Pokedex entry for the Pokemon

        :return: Pokedex entry
        :rtype: basestring
        """
        return random.choice(self.dex_entries)

# -*- coding: utf-8 -*-
""" Pokedex Entry class """


class PokedexEntry(object):
    """
    Representation of a Pokedex Entry
    """

    def __init__(self, pokemon_name, image_url, author):
        """
        Constructor for the Pokedex Entry

        :param pokemon_name: Name of the Pokemon the PokedexEntry is for
        :param image_url: URL of the uploaded image to associate with the entry
        :param author: Discord name of the user that uploaded the image
        :type pokemon_name: basestring
        :type image_url: basestring
        :type author: basestring
        """
        super(PokedexEntry).__init__()
        self.pokemon_name = pokemon_name
        self.image_url = image_url
        self.author = author

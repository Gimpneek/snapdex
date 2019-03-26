# -*- coding: utf-8 -*-
""" Pokedex Entry class """


class PokedexEntry(object):
    """
    Representation of a Pokedex Entry
    """

    def __init__(self, pokemon_name, image, original_message, details):
        """
        Constructor for the Pokedex Entry

        :param pokemon_name: Name of the Pokemon the PokedexEntry is for
        :param image: Image object uploaded
        :param original_message: Message that accompanied the upload
        :param details: Details on the Pokemon
        :type pokemon_name: basestring
        :type image: discord.Attachment
        :type original_message: discord.Message
        :type details: dict
        """
        super(PokedexEntry).__init__()
        self.pokemon_name = pokemon_name
        self.image = image
        self.author = original_message.author
        self.original_message = original_message
        self.details = details

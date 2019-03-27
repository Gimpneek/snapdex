from unittest import TestCase
from snapdex.snapdexClient import SnapdexClient


POKEMON_TEXT = 'This is a pic of {0} I took'


class TestGetPokemonNames(TestCase):

    def setUp(self):
        super(TestGetPokemonNames, self).setUp()
        self.pokemon_list = [
            'mew',
            'mewtwo'
        ]
        self.client = SnapdexClient(self.pokemon_list)

    def test_finds_pokemon(self):
        """
        Test that when passed text that contains one or more of the Pokemon
        in the pokemon_list that Pokemon(s) name is returned
        """
        text_to_test = POKEMON_TEXT.format('mew')
        found_pokemon = self.client.get_pokemon_names(text_to_test)
        self.assertEqual(found_pokemon[0], 'Mew')

    def test_name_contains_other_name(self):
        """
        Test that when the text contains the name of a Pokemon that contains
        another Pokemon's name (such as MewTwo containing Mew, Pidgeotto
        containing Pidgeot) that only the Pokemon that is specified is returned
        """
        text_to_test = POKEMON_TEXT.format('mewtwo')
        found_pokemon = self.client.get_pokemon_names(text_to_test)
        self.assertEqual(['Mewtwo'], found_pokemon)

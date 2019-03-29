from unittest import TestCase
from snapdex.pokemonListItem import PokemonListItem
from snapdex.tests.common import get_test_pokemon_list_item, TYPE_ONE, TYPE_TWO


class TestGetTypes(TestCase):

    def setUp(self):
        super(TestGetTypes, self).setUp()
        self.list_item = get_test_pokemon_list_item()

    def test_single_type(self):
        """
        Test that if the Pokemon has a single type, then only that type is
        returned
        """
        test_item = PokemonListItem('Test Pokemon', types=[TYPE_ONE])
        self.assertEqual(TYPE_ONE, test_item.get_types())

    def test_dual_type(self):
        """
        Test that if the Pokemon has dual typing, then both types are
        returned
        """
        self.assertEqual(
            '{0}/{1}'.format(TYPE_ONE, TYPE_TWO),
            self.list_item.get_types())

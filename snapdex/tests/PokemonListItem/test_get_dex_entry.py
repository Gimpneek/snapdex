from unittest import TestCase
from snapdex.pokemonListItem import PokemonListItem
from snapdex.tests.common import get_test_pokemon_list_item, DEX_ENTRY


class TestGetDexEntry(TestCase):

    def setUp(self):
        super(TestGetDexEntry, self).setUp()
        self.list_item = get_test_pokemon_list_item()

    def test_single_entry(self):
        """
        Test that if the Pokemon has a single dex entry, then only that
        dex entry is returned
        """
        self.assertEqual(DEX_ENTRY, self.list_item.get_dex_entry())

    def test_multiple_entries(self):
        """
        Test that if the Pokemon has more than one dex entry, then one of them
        is returned
        """
        dex_entries = ['a', 'b', 'c']
        test_item = PokemonListItem('Test', dex_entries=dex_entries)
        self.assertTrue(test_item.get_dex_entry() in dex_entries)

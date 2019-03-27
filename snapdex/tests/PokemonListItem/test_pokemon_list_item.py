from unittest import TestCase
from snapdex.pokemonListItem import PokemonListItem, MISSINGNO_SPRITE
from snapdex.tests.common import POKEMON_NAME, ALIAS_ONE, ALIAS_TWO, \
    POKEMON_NUMBER, TYPE_ONE, TYPE_TWO, DEX_ENTRY, SPRITE_URL, \
    get_test_pokemon_list_item


class TestPokemonListItem(TestCase):

    def setUp(self):
        super(TestPokemonListItem, self).setUp()
        self.list_item = get_test_pokemon_list_item()
        self.default_item = PokemonListItem('Test Pokemon')

    def test_name(self):
        """
        Test that the name of the Pokemon is correct
        """
        self.assertEqual(POKEMON_NAME, self.list_item.name)

    def test_no_name_raises(self):
        """
        Test that if no name is passed then an exception is raised
        """
        with self.assertRaises(Exception):
            PokemonListItem()

    def test_none_name_raises(self):
        """
        Test that is name is None then exception is raised
        """
        with self.assertRaises(Exception):
            PokemonListItem(None)

    def test_alias_list(self):
        """
        Test that the list of alias names for the Pokemon is correct
        """
        self.assertEqual([ALIAS_ONE, ALIAS_TWO], self.list_item.alias_list)

    def test_default_alias_list(self):
        """
        Test that if no alias list is passed then an empty list is returned
        """
        self.assertEqual([], self.default_item.alias_list)

    def test_number(self):
        """
        Test that the Pokemon's pokedex number is correct
        """
        self.assertEqual(POKEMON_NUMBER, self.list_item.number)

    def test_default_number(self):
        """
        Test that if no number is passed then the number is set to Missingno's
        number of 0
        """
        self.assertEqual(0, self.default_item.number)

    def test_types(self):
        """
        Test that the Pokemon's types are correct
        """
        self.assertEqual([TYPE_ONE, TYPE_TWO], self.list_item.types)

    def test_default_types(self):
        """
        Test that if no types are passed then an empty list is returned
        """
        self.assertEqual([], self.default_item.types)

    def test_dex_entries(self):
        """
        Test that the Pokemon's dex entry list is correct
        """
        self.assertEqual([DEX_ENTRY], self.list_item.dex_entries)

    def test_default_dex_entries(self):
        """
        Test that if no dex entries are passed then an empty list is returned
        """
        self.assertEqual([], self.default_item.dex_entries)

    def test_sprite(self):
        """
        Test that the Pokemon's sprite URL is correct
        """
        self.assertEqual(SPRITE_URL, self.list_item.sprite)

    def test_default_sprite(self):
        """
        Test that if no sprite is passed then Missingno's sprite from Gen 1 is
        used
        """
        self.assertEqual(MISSINGNO_SPRITE, self.default_item.sprite)

    def test_legendary_flag(self):
        """
        Test that the Pokemon's legendary flag is correct
        """
        self.assertEqual(True, self.list_item.legendary)

    def test_default_legendary(self):
        """
        Test that if the legendary flag isn't set then it's False
        """
        self.assertEqual(False, self.default_item.legendary)

    def test_mythic_flag(self):
        """
        Test that the Pokemon's mythic flag is correct
        """
        self.assertEqual(True, self.list_item.mythic)

    def test_default_mythic(self):
        """
        Test that if the mythic flag isn't set then it's False
        """
        self.assertEqual(False, self.default_item.mythic)

    def test_regional_flag(self):
        """
        Test that the Pokemon's regional flag is correct
        """
        self.assertEqual(True, self.list_item.regional)

    def test_default_regional(self):
        """
        Test that if the regional flag isn't set then it's False
        """
        self.assertEqual(False, self.default_item.regional)

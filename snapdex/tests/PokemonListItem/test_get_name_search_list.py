from unittest import TestCase
from snapdex.tests.common import get_test_pokemon_list_item, POKEMON_NAME, \
    ALIAS_ONE, ALIAS_TWO


class TestGetNameSearchList(TestCase):

    def setUp(self):
        super(TestGetNameSearchList, self).setUp()
        self.list_item = get_test_pokemon_list_item()

    def test_search_names(self):
        """
        Test that the official Pokemon name and any alias names are returned
        """
        self.assertEqual(
            r'\b{0}\b|\b{1}\b|\b{2}\b'.format(
                POKEMON_NAME.lower(),
                ALIAS_ONE.lower(),
                ALIAS_TWO.lower()
            ),
            self.list_item.get_name_search_list())

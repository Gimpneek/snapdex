from unittest import TestCase
import pytest


@pytest.mark.usefixtures("host")
class TestRequirements(TestCase):

    def setUp(self):
        super(TestRequirements, self).setUp()
        self.pokemon = self.host.file('/src/pokemon.csv')
        self.bot = self.host.file('/src/main.py')

    def test_pokemon_list(self):
        self.assertTrue(self.pokemon.exists)

    def test_bot(self):
        self.assertTrue(self.bot.exists)

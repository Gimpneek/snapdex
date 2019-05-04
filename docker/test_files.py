from unittest import TestCase
import pytest


@pytest.mark.usefixtures("host")
class TestRequirements(TestCase):
    """
    Check that the files needed to run the bot are in the Docker image
    """

    def setUp(self):
        super(TestRequirements, self).setUp()
        self.pokemon = self.host.file('/src/pokemon.csv')
        self.bot = self.host.file('/src/main.py')

    def test_pokemon_list(self):
        """
        Check that the pokemon.csv file needed to load in the Pokemon data
        is present in the image
        """
        self.assertTrue(self.pokemon.exists)

    def test_bot(self):
        """
        Check that the main.py file used to run the bot is present in the
        image
        """
        self.assertTrue(self.bot.exists)

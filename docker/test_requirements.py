from unittest import TestCase
import pytest


@pytest.mark.usefixtures("host")
class TestRequirements(TestCase):

    def setUp(self):
        super(TestRequirements, self).setUp()
        self.requirements = self.host.file('/src/requirements.txt').content_string

    def test_discord(self):
        self.assertIn('git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]', self.requirements)

    def test_pokedex_py(self):
        self.assertIn('pokedex.py==1.1.2', self.requirements)

    def test_python_3_7(self):
        python_version = self.host.command('python --version').stdout
        self.assertIn('3.7', python_version)

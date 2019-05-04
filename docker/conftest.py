import pytest
import subprocess
import os
import testinfra

# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope='class')
def host(request):
    # run a container
    discord_key = os.environ.get('DISCORD_KEY')
    docker_id = subprocess.check_output(
        [
            'docker',
            'run',
            '-d',
            '--env',
            'DISCORD_KEY={0}'.format(discord_key),
            'gimpneek/snapdex'
        ]
    ).decode().strip()
    # return a testinfra connection to the container
    host = testinfra.get_host("docker://" + docker_id)
    request.cls.host = host
    yield host
    # at the end of the test suite, destroy the container
    subprocess.check_call(['docker', 'rm', '-f', docker_id])

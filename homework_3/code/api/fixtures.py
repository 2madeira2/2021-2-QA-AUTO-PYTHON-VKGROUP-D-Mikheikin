import os
import pytest
import random
import string

@pytest.fixture(scope='function')
def logo_path(repo_root):
    return os.path.join(repo_root, 'api', '../resources/logo.png')


@pytest.fixture(scope="function")
def get_random_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=7))

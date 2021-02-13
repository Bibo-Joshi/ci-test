import warnings

from package import CustomWarning


class TestStuff:
    def test_env_var(self):
        warnings.warn('Hi there', category=CustomWarning)

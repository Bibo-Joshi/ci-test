import os

class TestStuff:
    def test_env_var(self):
        print(repr(os.getenv('TEST_NO_PASSPORT', 'NO SUCH ENVVAR')))

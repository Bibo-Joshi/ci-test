import os

print(repr(os.getenv('TEST_NO_PASSPORT', 'NO SUCH ENVVAR')))

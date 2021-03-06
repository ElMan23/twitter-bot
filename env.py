################################################################
# 
# Just to experiment with ENV vars
# 
################################################################

import os

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
# PASSWORD = os.environ.get('API_PASSWORD')
PASSWORD = os.environ['API_PASSWORD']

EXT = os.environ['EXT']
print(EXT)

print(USER)
print(PASSWORD)

# # Getting non-existent keys
# FOO = os.getenv('FOO') # None
# BAR = os.environ.get('BAR') # None
# BAZ = os.environ['BAZ'] # KeyError: key does not exist.
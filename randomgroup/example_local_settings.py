import dj_database_url
DATABASES = {'default': dj_database_url.parse('postgres://db:pass@localhost/user')}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'FIFTY_RANDOM_CHARACTERS'

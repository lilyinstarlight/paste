# address to listen on
addr = ('', 8080)

# log locations
log = '/var/log/paste/paste.log'
httplog = '/var/log/paste/http.log'

# where service is located
service = 'https://paste.fooster.io'

# where store is located
store = 'store.fooster.io'
store_https = True
store_endpoint = '/'

# interval for storing pastes
interval = 604800  # 1 week

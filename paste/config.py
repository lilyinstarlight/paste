# address to listen on
addr = ('', 8000)

# log locations
log = '/var/log/paste/paste.log'
httplog = '/var/log/paste/http.log'

# template directory to use
import os.path
template = os.path.dirname(__file__) + '/html'

# where service is located
service = 'https://paste.lily.flowers'

# where store is located
store = 'https://store.lily.flowers'

# datetime timezone
timezone = 'UTC'

# interval for storing pastes
interval = 604800  # 1 week

# datetime format
datetime_format = '%Y-%m-%d %H:%M %Z'

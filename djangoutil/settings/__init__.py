from .base import *

# you need to set "environment = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
try:
    if os.environ['environment'] == 'prod':
        from .prod import *
    else:
        from .dev import *
except KeyError:
    from .dev import *

#!/usr/bin/env python3
# more info: https://pypi.org/project/python-crontab/

### Acknowledgements
# Getting UTC time zone and conversion on - https://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
# Timezone List on - https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones

from datetime import datetime
from pytz import timezone
from sense_hat import SenseHat

# Get the UTC object
utcTimeZone = datetime.now(timezone('UTC'))

# Convert to Melbourne time zone
aestTimeZone = utcTimeZone.astimezone(timezone('Australia/Melbourne'))

# Declare a SenseHAT object and display Melbourne time zone
sense = SenseHat()
sense.show_message('Time is {}'.format(aestTimeZone), scroll_speed=0.05)


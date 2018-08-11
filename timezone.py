#!/usr/bin/env python3
# more info: https://pypi.org/project/python-crontab/

### Acknowledgements
# Getting UTC time zone and conversion on - https://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
# Timezone List on - https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones

from datetime import datetime
from pytz import timezone
from sense_hat import SenseHat


def convert_time_zone():

    # Get the UTC object
    utx_time_zone = datetime.now(timezone('UTC'))

    # Convert to Melbourne time zone
    aest_time_zone = utx_time_zone.astimezone(timezone('Australia/Melbourne'))

    # Declare a SenseHAT object and display Melbourne time zone
    # sense = SenseHat()
    # sense.show_message('Time is {}'.format(aestTimeZone), scroll_speed=0.05)

    return aest_time_zone



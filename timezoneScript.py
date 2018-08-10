#!/usr/bin/env python3
# more info: https://pypi.org/project/python-crontab/

### Acknowledgements
# Getting UTC time zone and conversion on - https://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
# Timezone List on - https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones

import pytz
from pytz import timezone
import tzlocal

def timezoneConverter(value, format="%I:%M %p"):
    tz = pytz.timezone('Australia/Melbourne')
    utc = pytz.timezone('UTC')
    value = utc.localize(value, is_dst = None).astimezone(pytz.utc)
    local_dateTime = value.astimezone(tz)
    return local_dateTime.strftime(format)



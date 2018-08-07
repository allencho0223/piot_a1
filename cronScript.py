#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add new cron job
job  = cron.new(command='/home/pi/iot/ass1/data_collector.py')

#job settings
job.minute.every(1)
cron.write()

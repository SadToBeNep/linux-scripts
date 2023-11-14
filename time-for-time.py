import datetime
import pytz

option = str(input("Tell me the time, or just press enter to use current local time: "))

zones = pytz.all_timezones

print(datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo)
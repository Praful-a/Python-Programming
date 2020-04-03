import datetime
import pytz
d = datetime.date(2016, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)

tday = datetime.date.today()
print(tday.year)
print(tday.day)
print(tday.month)
print(tday.weekday())
print(tday.isoweekday())
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(tday - tdelta)
date2 = date1 + date2
timedelta = date1 + date2

bday = datetime.date(2020, 6, 13)
till_bday = bday - tday
print(till_bday.total_seconds())

t = datetime.time
print(t)

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)
print(t.minute)

t = datetime.datetime(2020, 3, 3, 12, 30, 45, 100000)
print(t)
print(t.date())
print(t.time())

t = datetime.datetime(2020, 3, 3, 12, 30, 45, 100000)

tdelta = datetime.timedelta(days=7)
print(t + tdelta)

tdelta = datetime.timedelta(hours=12)
print(t + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

for tz in pytz.all_timezones:
    print(tz)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

dt_mtn = mtn_tz.localize(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_mtn)
print(dt_east)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'April 03, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

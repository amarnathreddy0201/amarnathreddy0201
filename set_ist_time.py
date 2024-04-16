from datetime import datetime,timedelta,timezone
# current_utc_datetime = datetime.utcnow()
# Use timezone-aware objects to represent datetimes in UTC
current_utc_datetime = datetime.now(timezone.utc)
ist_offset = timedelta(hours=5, minutes=30)
current_ist_datetime = current_utc_datetime + ist_offset
ist_date = current_ist_datetime.date().isoformat()
ist_time = current_ist_datetime.time().isoformat(timespec='milliseconds')
print(ist_date)
print(ist_time)

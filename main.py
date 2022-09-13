from icalendar import Calendar, Event, vCalAddress, vText, Alarm
import pytz
from datetime import datetime
import os
from pathlib import Path
from variables import mailto_email, organizer_email, organizer_name, organizer_role, summary, location, year, month, day, start_hour, end_hour, minute, second


start_time = datetime(year, month, day, start_hour, minute,
                      second,  tzinfo=pytz.timezone("America/Chicago"))
end_time = datetime(year, month, day, end_hour, minute,
                    second, tzinfo=pytz.timezone("America/Chicago"))

#
cal = Calendar()
# cal.add('attendee', mailto_email)
# cal.add('attendee', mailto_email)


event = Event()
event.add('summary', summary)
event.add('dtstart', start_time)
event.add('dtend', end_time)
event.add('dtstamp', datetime.now())
event.add('priority', 5)

organizer = vCalAddress(organizer_email)
organizer.params['cn'] = vText(organizer_name)
# organizer.params['role'] = vText(organizer_role)
event['organizer'] = organizer
event['location'] = vText(location)

# add Alarm
alarm = Alarm()
alarm.add("TRIGGER;RELATED=START", "-PT{0}M".format('5'))
alarm.add('action', 'display')
alarm.add('description', summary)
event.add_component(alarm)


# Adding events to calendar
cal.add_component(event)

directory = str(Path(__file__).parent) + "/"
print("ics file will be generated at ", directory)
f = open(os.path.join(directory, f'{summary.replace(" ", "_")}.ics'), 'wb')
f.write(cal.to_ical())
f.close()

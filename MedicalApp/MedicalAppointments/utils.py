import datetime
import pytz

from django.utils import timezone

from .models import Doctor


def get_clinics_by_specialty(specialty):
    doctors = Doctor.objects.filter(specialty__specialty=specialty)
    # Return a unique list by converting list to set and converting back
    return list(set([d.clinic for d in doctors]))


def get_dates_from_now():
    # return 7 days starting today
    today = timezone.now().date()
    dates = []
    for day_delta in range(7):
        dates.append(today + datetime.timedelta(days=day_delta))
    return dates


def check_booking_in_timeslot(timeslot_start, interval, booking_time):
    index = 0
    for booking in booking_time:
        if timeslot_start <= booking < timeslot_start + interval:
            # Return the index of booking_time array
            return index
        index += 1
    # Return index of -1 if no booking exist in the time slot
    return -1


def get_time_table(bookings, table_start, table_end, table_interval):
    booking_time = [booking.time for booking in bookings]

    TZ_UTC = pytz.utc
    local_tz = timezone.get_default_timezone()

    start_hour = datetime.time(hour=table_start, tzinfo=local_tz)
    end_hour = datetime.time(hour=table_end, tzinfo=local_tz)
    interval = datetime.timedelta(minutes=table_interval)
    time_table = []
    dates = get_dates_from_now()

    first_row = []
    for day in dates:
        timeslot_start = datetime.datetime.combine(day, start_hour).astimezone(TZ_UTC)
        index = check_booking_in_timeslot(timeslot_start, interval, booking_time)
        if index != -1:
            first_row.append((timeslot_start, bookings[index].patient.user))
        else:
            first_row.append((timeslot_start, None))

    time_table.append(first_row)

    while time_table[-1][0][0].timetz() < end_hour:
        table_row = []
        for day in time_table[-1]:
            timeslot_start = day[0] + interval
            index = check_booking_in_timeslot(timeslot_start, interval, booking_time)
            if index != -1:
                table_row.append((timeslot_start, bookings[index].patient.user))
            else:
                table_row.append((timeslot_start, None))
        time_table.append(table_row)

    return time_table
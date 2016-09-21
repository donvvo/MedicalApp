import datetime
import pytz

from django.utils import timezone

from .models import Doctor

local_tz = timezone.get_default_timezone()


def get_clinics_by_specialty(specialty):
    doctors = Doctor.objects.filter(specialty__specialty=specialty)
    # Return a unique list by converting list to set and converting back
    return list(set([d.clinic for d in doctors if d.clinic is not None]))


def get_dates_from_now():
    # return 7 days starting today
    today = timezone.now().date()
    dates = []
    for day_delta in range(7):
        dates.append(today + datetime.timedelta(days=day_delta))
    return dates


def check_booking_in_timeslot(timeslot_start, interval, booking_time):
    index_array = []
    index = 0
    for booking in booking_time:
        if timeslot_start <= booking < timeslot_start + interval:
            # Return the index of booking_time array
            index_array.append(index)
        index += 1
    # Return index of -1 if no booking exist in the time slot
    return index_array


def get_min_start_hour(start_end_hour):
    start_hours = [hour[0] for hour in start_end_hour if hour[0] is not None]
    return min(start_hours) if start_hours else datetime.time(hour=9, tzinfo=local_tz) # default


def get_max_end_hour(start_end_hour):
    start_hours = [hour[1] for hour in start_end_hour if hour[1] is not None]
    return max(start_hours) if start_hours else datetime.time(hour=18, tzinfo=local_tz) # default


def get_column_for_a_day(day, start_end_hour, min_hour, max_hour, interval, bookings, num_doctor):
    booking_time = [booking.time for booking in bookings]

    column = []
    timeslot_start = datetime.datetime.combine(day, min_hour).astimezone(local_tz)

    time_row = timeslot_start

    while time_row.timetz() < max_hour:
        this_time = time_row.timetz()
        if not start_end_hour[0] or not start_end_hour[1]:
            column.append((time_row, -1))
        elif this_time < start_end_hour[0] or this_time > start_end_hour[1]:
            column.append((time_row, -1))
        else:
            index = check_booking_in_timeslot(time_row, interval, booking_time)
            if index != [] and len(index) == num_doctor:
                column.append((time_row, bookings[index[0]].patient.user))
            else:
                column.append((time_row, None))

        time_row = time_row + interval

    return column


def get_time_table(bookings, clinic, table_interval, num_doctor):
    # start and end hour in tuple, starting Monday
    if clinic:
        start_end_hour_naive = [
            (clinic.start_time_mon, clinic.end_time_mon),
            (clinic.start_time_tue, clinic.end_time_tue),
            (clinic.start_time_wed, clinic.end_time_wed),
            (clinic.start_time_thurs, clinic.end_time_thurs),
            (clinic.start_time_fri, clinic.end_time_fri),
            (clinic.start_time_sat, clinic.end_time_sat),
            (clinic.start_time_sun, clinic.end_time_sun)
        ]
    else:
        start_end_hour_naive = [
            (None, None),
            (None, None),
            (None, None),
            (None, None),
            (None, None),
            (None, None),
            (None, None)
        ]
    start_end_hour = []
    for element in start_end_hour_naive:
        if element[0] and element[1]:
            start_end_hour.append(
                (element[0].replace(tzinfo=local_tz), element[1].replace(tzinfo=local_tz))
            )
        else:
            start_end_hour.append((None, None))
    min_start_hour = get_min_start_hour(start_end_hour)
    max_end_hour = get_max_end_hour(start_end_hour)

    interval = datetime.timedelta(minutes=table_interval)
    dates = get_dates_from_now()

    columns = []

    for date in dates:
        columns.append(get_column_for_a_day(date, start_end_hour[date.weekday()], min_start_hour,
            max_end_hour, interval, bookings, num_doctor))

    timetable = []
    for index in range(len(columns[0])):
        timetable.append([column[index] for column in columns])

    return timetable


def check_clinic_booking_in_timeslot(timeslot_start, interval, bookings):
    booking_array = []
    for booking in bookings:
        if timeslot_start <= booking.time < timeslot_start + interval:
            # Append this booking to booking_array
            # Specifically only name of doctor will be used for now
            booking_array.append(booking.doctor.user)
    return booking_array


def get_clinic_column_for_a_day(day, start_end_hour, min_hour, max_hour, interval, bookings):
    column = []
    timeslot_start = datetime.datetime.combine(day, min_hour).astimezone(local_tz)

    time_row = timeslot_start

    while time_row.timetz() < max_hour:
        this_time = time_row.timetz()
        if not start_end_hour[0] or not start_end_hour[1]:
            column.append((time_row, -1))
        elif this_time < start_end_hour[0] or this_time > start_end_hour[1]:
            column.append((time_row, -1))
        else:
            booking_array = check_clinic_booking_in_timeslot(time_row, interval, bookings)
            if booking_array != []:
                column.append((time_row, booking_array))
            else:
                column.append((time_row, None))

        time_row = time_row + interval

    return column


def get_clinic_time_table(bookings, clinic, table_interval):
    # start and end hour in tuple, starting Monday
    if clinic:
        start_end_hour_naive = [
            (clinic.start_time_mon, clinic.end_time_mon),
            (clinic.start_time_tue, clinic.end_time_tue),
            (clinic.start_time_wed, clinic.end_time_wed),
            (clinic.start_time_thurs, clinic.end_time_thurs),
            (clinic.start_time_fri, clinic.end_time_fri),
            (clinic.start_time_sat, clinic.end_time_sat),
            (clinic.start_time_sun, clinic.end_time_sun)
        ]
    else:
        start_end_hour_naive = [
            (None, None),
            (None, None),
            (None, None),
            (None, None),
            (None, None),
            (None, None),
            (None, None)
        ]
    start_end_hour = []
    for element in start_end_hour_naive:
        if element[0] and element[1]:
            start_end_hour.append(
                (element[0].replace(tzinfo=local_tz), element[1].replace(tzinfo=local_tz))
            )
        else:
            start_end_hour.append((None, None))
    min_start_hour = get_min_start_hour(start_end_hour)
    max_end_hour = get_max_end_hour(start_end_hour)

    interval = datetime.timedelta(minutes=table_interval)
    dates = get_dates_from_now()

    columns = []

    for date in dates:
        columns.append(get_clinic_column_for_a_day(date, start_end_hour[date.weekday()], min_start_hour,
            max_end_hour, interval, bookings))

    timetable = []
    for index in range(len(columns[0])):
        timetable.append([column[index] for column in columns])

    return timetable

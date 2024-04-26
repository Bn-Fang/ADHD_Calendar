import streamlit as st
from streamlit_calendar import calendar
from Cal import *
from datetime import datetime, timedelta, time
import base64
import plotly.express as px
from collections import defaultdict
from canvasTimelines import canvasHelper

# Example API data structure
# api_output = defaultdict(list, {
#     'EECS 495 002 WN 2024': [
#         {'name': 'Final presentation', 'due_date': datetime(2024, 4, 27, 3, 59, 59), 'url': 'https://umich.instructure.com/courses/669192/assignments/2348319'},
#         {'name': 'Final report', 'due_date': datetime(2024, 4, 27, 3, 59, 59), 'url': 'https://umich.instructure.com/courses/669192/assignments/2348321'},
#         {'name': 'Final video', 'due_date': datetime(2024, 4, 27, 3, 59, 59), 'url': 'https://umich.instructure.com/courses/669192/assignments/2348322'},
#         {'name': 'Any feedback for us?', 'due_date': datetime(2024, 4, 29, 3, 59, 59), 'url': 'https://umich.instructure.com/courses/669192/assignments/2348323'}
#     ]
# })
def canvas(calendar_id):
    api_output = canvasHelper()

    # Assuming `calendarID` is predefined
    calendarID = calendar_id

    # Iterate over each course or event group
    for course, events in api_output.items():
        coursename = course.split()
        coursename = coursename[0] + ' ' + coursename[1]
        if events:  # Check if there are any events
            for event in events:
                title = event['name']
                due_date = event['due_date']
                url = event.get('url', '')

                # Create an event with a slight buffer before the due date as the start time
                start = (due_date - timedelta(minutes=30)).isoformat()
                end = due_date.isoformat()
                description = f"Due Date: {due_date}\nDetails: {url}"

                # Call the function to create the event on the calendar
                # TODO: WE NEED TO MODIFY Cal.py TO ADD THE DESCRIPTION AND URL
                create_event(calendarID, title, start, end, all_day=True, course_name=coursename, url=url)

                print(f"Event created: {title} on {due_date}")

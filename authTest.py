import streamlit as st
from auth import *
from Cal import get_calendar_service
import datetime
from datetime import datetime, timedelta



def create_event( ):

    print("Create an event")
    a = input("Describe the event: ")
    service = get_calendar_service()

    date = datetime.now().date()
    today = datetime(date.year, date.month, date.day, 10) + timedelta(days=0)
    start = today.isoformat()
    end = (today + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(calendarId='primary',
                                           body={
                                               "summary": 'CALENDAR AUTOMATION',
                                               "description": a,
                                               "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
                                               "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                                           }
                                           ).execute()

    st.write("Calendar Automation has created an event")
    st.write("Id: ", event_result['id'])
    st.write("Summary: ", event_result['summary'])
    st.write("Starts At: ", event_result['start']['dateTime'])
    st.write("Ends At: ", event_result['end']['dateTime'])


if __name__ == '__main__':
    st.title("Streamlit Oauth Login")
        
    if st.button("Login with Google"):
        get_calendar_service()

    if st.button("create event"):
        create_event()
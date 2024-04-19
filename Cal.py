'''
Before Starting using Google OAuth SDK for Python, install
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
for errors with the crypto module
pip uninstall pycryptodome
first.
'''

'''
Import the following libraries
'''
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import googleapiclient
from datetime import datetime, timedelta, time
import streamlit as st


# You can change the scope of the application, make sure to delete token.pickle file first
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'     # Give path to your credentials.json file


def get_calendar_service():

    cred = None

    '''
    The file token.pickle stores the user's access and refresh tokens, and is created automatically when
    the authorization flow completes for the first time. In other words when the user give access to this 
    channel
    '''

    if os.path.exists('token.pickle'):
        with open('token.pickle','rb') as token:
            cred = pickle.load(token)
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            print(flow)
            cred = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(cred, token)
    service = build('calendar','v3',credentials=cred)
    return service

def get_user_service():
    
    cred = None

    '''
    The file token.pickle stores the user's access and refresh tokens, and is created automatically when
    the authorization flow completes for the first time. In other words when the user give access to this 
    channel
    '''

    if os.path.exists('token.pickle'):
        with open('token.pickle','rb') as token:
            cred = pickle.load(token)
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            print(flow)
            cred = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(cred, token)
    service = build('cloudidentity','v1beta1',credentials=cred)
    return service


def signOut():
    os.remove('token.pickle')
    print("Token has been removed")

def get_calendar_ID(CalenderName):
    calendar_list = get_calendar_service().calendarList().list().execute()
    calendarID = ""
    for calendar_list_entry in calendar_list['items']:
        if calendar_list_entry['summary'] == CalenderName:
            calendarID = calendar_list_entry['id']
            break
    if calendarID == "":
        calendarTemplate = {
            'summary': 'Adhd',
            'timeZone': 'America/New_York'
        }
        created_calendar = get_calendar_service().calendars().insert(body=calendarTemplate).execute()
        calendarID = created_calendar['id']
    return calendarID


'''
You must create two .py files in order to manage it smoothly, one name as cal_setup.py and
other as main.py. main.py is the file where all the functionality will take place while
cal_setup.py will form connection with Google Calendar API and creates authorization token.
CALENDAR AUTOMATION USING GOOGLE CALENDAR API AND OAUTH2
Requirements:
googleapiclient, datetime
REMEMBER>>>>>>>>>>>>>>>>
1. Before running this file make sure you have setup your Google Calendar API and OAuth screen
also you have to download credentials.json file which will be availble on you Google Calendar API dashboard.
2. Make sure you have given path to credentials.json file
3. And, you have to (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib)
'''

def get_name():
    calendar_list = get_calendar_service().calendarList().list().execute()
    calendarID = ""
    for calendar_list_entry in calendar_list['items']:
        if(calendar_list_entry.get('primary')):
            return(str(calendar_list_entry['id']).split("@")[0])
    
    

def list_cal():

    print("List all calendar")
    service = get_calendar_service()

    print('Getting list of calendars')
    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get('items', [])

    if not calendars:
        print('No calendars found.')
    for calendar in calendars:
        summary = calendar['summary']
        id = calendar['id']
        primary = "Primary" if calendar.get('primary') else ""
        print("%s\t%s\t%s" % (summary, id, primary))

# def create_event():

#     print("Create an event")
#     a = input("Describe the event: ")
#     service = get_calendar_service()

#     date = datetime.now().date()
#     today = datetime(date.year, date.month, date.day, 10) + timedelta(days=0)
#     start = today.isoformat()
#     end = (today + timedelta(hours=1)).isoformat()

#     event_result = service.events().insert(calendarId='primary',
#                                            body={
#                                                "summary": 'CALENDAR AUTOMATION',
#                                                "description": a,
#                                                "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
#                                                "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
#                                            }
#                                            ).execute()

#     print("Calendar Automation has created an event")
#     print("Id: ", event_result['id'])
#     print("Summary: ", event_result['summary'])
#     print("Starts At: ", event_result['start']['dateTime'])
#     print("Ends At: ", event_result['end']['dateTime'])


def list_event(CalendarID):
    import datetime

    # print("List 10 upcoming events")
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.now().isoformat() + 'Z'  # 'Z' indicates UTC time
    # print('Getting List of 10 events')
    events_result = service.events().list(calendarId=CalendarID, timeMin=now,
                                          maxResults=20, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result['items']

    if not events:
        print('No upcoming events found.')
    eventsOut = []
    # print('Calendar ID: ', CalendarID, events_result['items'])
    for event in events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start, event)
        calenderItem = {
          "title": str(event['summary']),
        "color": event['colorId'] if 'colorId' in event else "#fca903",
        "start": event['start']['dateTime'] if 'dateTime' in event['start'] else event['start']['date'],
        "end": event['end']['dateTime'] if 'dateTime' in event['end'] != None else event['end']['date'],
        "resourceId": str(event['summary']).split(" | ")[1] if len(str(event['summary']).split(" | ")) > 1 else "a",
        }
        eventsOut.append(calenderItem)
    return eventsOut
        
        
        
        
        

# {
#         "title": "Event 14",
#         "color": "#3D9DF3",
#         "start": "2023-07-17T09:30:00",
#         "end": "2023-07-17T11:30:00",
#         "resourceId": "b",
#     }



def update_event():

    print("Update an event")
    service = get_calendar_service()
    al = input("Enter Calender ID: ")
    eid = input("Enter Event ID: ")
    a = input("Describe the new event: ")

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 9) + timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=2)).isoformat()

    event_result = service.events().update(
        calendarId=al,
        eventId=eid,
        body={
        "summary": 'AAKASH --- CALENDAR AUTOMATION',
        "description": a,
        "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
        "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
        },
         ).execute()


    print("Updated Event: ", eid)
    print("Id: ", event_result['id'])
    print("Summary: ", event_result['summary'])
    print("Starts At: ", event_result['start']['dateTime'])
    print("Ends At: ", event_result['end']['dateTime'])

def delete_event():

    print("Delete an event")
    service = get_calendar_service()
    cal = input("Enter Calender ID: ")
    eid = input("Enter Event ID: ")
    try:
        service.events().delete(
            calendarId=cal,
            eventId=eid,
        ).execute()
    except googleapiclient.errors.HttpError:
        print("Failed to delete event")

    print("Event deleted")


def create_event(CalendarID, eventDiscription, start, end ):
    # date = datetime.now().date()
    # today = datetime(date.year, date.month, date.day, 10) + timedelta(days=0)
    # start = today.isoformat()
    # end = (today + timedelta(hours=1)).isoformat()
    service = get_calendar_service()
    event_result = service.events().insert(calendarId=CalendarID,
                                           body={
                                               "summary": 'Automated Event '+ eventDiscription,
                                               "description": eventDiscription,
                                               "start": {"dateTime": start, "timeZone": 'America/New_York'},
                                               "end": {"dateTime": end, "timeZone": 'America/New_York'},
                                           }
                                           ).execute()

    st.write("Calendar Automation has created an event")
    st.write("Id: ", event_result['id'])
    st.write("Summary: ", event_result['summary'])
    st.write("Starts At: ", event_result['start']['dateTime'])
    st.write("Ends At: ", event_result['end']['dateTime'])

options = ["Eating", "Vyvance", "Study", "Sleep", "Work", "Exercise", "Meditation", "Reading", "Coding", "Meeting", "Break", "Other"]

Presets = {
    "Eating": [datetime.now(), datetime.now(), time(1,20), time(1,30)], 
    "Vyvance": [datetime.now(), datetime.now(),time(1,30), timedelta(hours=12)],
    "Study": [datetime.now(), datetime.now(),time(1,20), time(1,30)],
    "Sleep": [datetime.now(), datetime.now(),time(1,20),time(1,30)],
    "Work": [datetime.now(), datetime.now(),time(1,20),time(1,30)],
    "Exercise": [datetime.now(), datetime.now(),time(1,20),time(1,30)],
    "Meditation": [datetime.now(), datetime.now(),time(1,20),time(1,30)],
    "Reading": [datetime.now(), datetime.now(),time(1,20),time(1,30)],
    "Coding": [datetime.now(), datetime.now(),time(1,20),time(1,30)],
    "Meeting": [datetime.now(), datetime.now(),time(1,20),time(1,30)],
    "Break": [datetime.now(), datetime.now(),time(1,20),time(1,30)],
    "Other": [datetime.now(), datetime.now(), datetime.now(), (datetime.now()+timedelta(hours=1))],
}

def login():
    if os.path.exists('token.pickle'):
        st.sidebar.write("You're logged in as", get_name())
        
        st.session_state.loggedIn = True
        st.session_state.calendarID = get_calendar_ID("Adhd")
        st.session_state.events = list_event(st.session_state.calendarID)
        print("events", st.session_state.events)
        
        if st.sidebar.button("Logout"):
            os.remove('token.pickle')
            st.write("You're logged out")
            st.session_state.loggedIn = False
            st.rerun()    
    else:
        st.sidebar.write("You're not logged in")
        if st.sidebar.button("Login with Google", key="login"):
            get_calendar_service()
            

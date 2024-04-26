import streamlit as st
from datetime import datetime, timedelta
from Cal import *

options = ["Eating", "Vyvance", "Study", "Sleep", "Work", "Exercise", "Meditation", "Reading", "Coding", "Meeting", "Break", "Other"]

Presets = {
    "Eating": [datetime.now(), datetime.now()+timedelta(days=1), datetime(2024, 6, 21, 3,4), time(1,30)], 
    "Vyvance": [datetime.now(), datetime.now(),datetime(2024, 6, 21, 3,4), timedelta(hours=12)],
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




def eventMaker():
    if st.session_state.loggedIn == True:
        st.session_state.description = st.selectbox(
        "Describe the event",
        options,
        index=0,
        placeholder="Eating",
        )
        st.session_state.AllDay = st.checkbox("All Day Event")
        st.session_state.timeConflict = st.checkbox("Allow Time Conflict")
        date, time= st.columns(2)
        
        submit_button = st.button(label='Submit')
        auto_place = st.button(label='Auto Place')
        # submit_button = st.button(label='Submit')
        
        
        timeInput = [Presets[st.session_state.description][0], Presets[st.session_state.description][1],Presets[st.session_state.description][2], Presets[st.session_state.description][3]]
        
        if st.session_state.description == "Sleep":
            timeInput = [Presets[st.session_state.description][0], Presets[st.session_state.description][1],Presets[st.session_state.description][2], Presets[st.session_state.description][3]]

        with date:
            startDate = st.date_input("Select Date", key="startDate", value=timeInput[0])
            endDate = st.date_input("Select endDate", key="endDate", value=timeInput[1] )
        with time:
            
            if st.session_state.AllDay == True:
                startTime = st.time_input("Select Time", key="disabledStart", disabled=True)
                endTime = st.time_input("Select endTime" , key="disabledEnd", disabled=True)
            else:
                startTime = st.time_input("Select Time", key="startTime", value= timeInput[2].time(), step=timedelta(minutes=5))
                if st.session_state.description == "Vyvance":
                    endTime = st.time_input("Select endTime" , key="endTime", value= (timeInput[2] + timeInput[3]).time(), step=timedelta(minutes=5), disabled=True)
                else:
                    endTime = st.time_input("Select endTime" , key="endTime", value= (timeInput[3]), step=timedelta(minutes=5))
                
        startDate = datetime.combine(startDate, startTime)
        start = startDate.isoformat()
        endDate = datetime.combine(endDate, endTime)
        end = endDate.isoformat()

        if submit_button:
            print(st.session_state.description, start, end)
            create_event(st.session_state.calendarID, st.session_state.description, start, end, st.session_state.AllDay, st.session_state.timeConflict)    
            st.write("Event Created")
        
        if auto_place:
            place_event(st.session_state.calendarID, st.session_state.description, start, end)
            st.write("Event Created")
            
    else:
        st.write("Please login to create events")
        if st.button("Login with Google"):
            get_calendar_service()


import streamlit as st
from datetime import datetime, timedelta
from Cal import *

options = ["Eating", "Vyvance (12 hr)", "Study", "Sleep (8 hr)", "Work (2 hr)", "Exercise (30 min)", "Break", "Other"]

Presets = {
    "Eating": [datetime.now(), datetime.now(), datetime(2024, 6, 21, 7,), time(8,30), False, True  ], 
    
    "Vyvance (12 hr)": [datetime.now(), datetime.now(),
                datetime(datetime.now().year,datetime.now().month,datetime.now().day, 8,0), 
                timedelta(hours=12), False, True],
    
    "Study": [datetime.now(), datetime.now(),time(1,20), time(1,30), False, True],
    
    "Sleep (8 hr)": [datetime.now(), 1,time(1,20),timedelta(hours=8), False, True],
    
    
    "Work (2 hr)": [datetime.now(), datetime.now(),datetime.now(), datetime.now()+ timedelta(hours=2), False, True],
    "Exercise (30 min)": [datetime.now(), datetime.now(),datetime.now(), datetime.now()+ timedelta(minutes=30), False, True],
    "Break": [datetime.now(), datetime.now(),time(1,20),time(1,30), False, True],
    "Other": [datetime.now(), datetime.now(), datetime.now(), datetime.now(), False, True],
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
        
        with date:
            startDate = st.date_input("Select Date", key="startDate", value=timeInput[0])
        
            if (type(timeInput[1]) == int):
                endDate = st.date_input("Select endDate", key="endDateDelta", value=startDate + timedelta(days=timeInput[1]), disabled=True)
            elif st.session_state.description == "Sleep (8 hr)":
                endDate = st.date_input("Select endDate", key="endDateDelta", value=startDate + timedelta(days=1), disabled=True)
            else:
                endDate = st.date_input("Select endDate", key="endDate", value=timeInput[1] )
        with time:
            
            if st.session_state.AllDay == True:
                startTime = st.time_input("Select Time", key="disabledStart", disabled=True)
                endTime = st.time_input("Select endTime" , key="disabledEnd", disabled=True)
            else:
                startTime = st.time_input("Select Time", key="startTime", value= datetime(endDate.year,endDate.month,endDate.day,timeInput[2].hour, timeInput[2].minute, timeInput[2].second) , step=timedelta(minutes=5))
                
                if st.session_state.description == "Vyvance (12 hr)" or st.session_state.description == "Sleep (8 hr)" or st.session_state.description == "Exercise (30 min)":
                    endTime = st.time_input("Select endTime" , key="endTime", value= datetime(endDate.year,endDate.month,endDate.day,startTime.hour, startTime.minute, startTime.second) + timeInput[3], step=timedelta(minutes=5), disabled=True)
                else:
                    endTime = st.time_input("Select endTime" , key="endTime", value= datetime(endDate.year,endDate.month,endDate.day,timeInput[3].hour, timeInput[3].minute, timeInput[3].second) , step=timedelta(minutes=5))
            st.session_state.startTimeVal = startTime
        startDate = datetime.combine(startDate, startTime)
        start = startDate.isoformat()
        endDate = datetime.combine(endDate, endTime)
        end = endDate.isoformat()

        if submit_button:
            print(st.session_state.description, start, end)
            create_event(st.session_state.calendarID, st.session_state.description, start, end, st.session_state.AllDay, st.session_state.timeConflict)    
            st.write("Event Created")
            st.balloons()
        
        if auto_place:
            place_event(st.session_state.calendarID, st.session_state.description, start, end)
            st.write("Event Created")
            st.balloons()
            
    else:
        st.write("Please login to create events")
        if st.button("Login with Google"):
            get_calendar_service()

